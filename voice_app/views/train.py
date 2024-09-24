from django.shortcuts import render, redirect
from django.conf import settings
from voice_app.models import VoiceModel
from voice_app.forms import VoiceModelForm
from volcano_engine.train import train_voice_model
import os
import uuid


def train_voice(request):
    if request.method == 'POST':
        form = VoiceModelForm(request.POST, request.FILES)
        if form.is_valid():
            audio_file = request.FILES['audio_file']
            name = form.cleaned_data['name']

            training_audio_dir = os.path.join(
                settings.MEDIA_ROOT, 'training_audio')
            os.makedirs(training_audio_dir, exist_ok=True)

            file_name = f'{uuid.uuid4()}.m4a'
            file_path = os.path.join(training_audio_dir, file_name)

            with open(file_path, 'wb+') as destination:
                for chunk in audio_file.chunks():
                    destination.write(chunk)

            try:
                response = train_voice_model(
                    settings.VOLCANO_ACCESS_KEY,
                    settings.VOLCANO_SECRET_KEY,
                    file_path
                )
                if response['code'] == 3000:
                    speaker_id = response['data']['speaker_id']
                    VoiceModel.objects.create(name=name, speaker_id=speaker_id)
                    os.remove(file_path)
                    return redirect('voice_list')
                else:
                    form.add_error(None, f"API 错误: {
                                   response.get('message', '未知错误')}")
            except Exception as e:
                form.add_error(None, f"发生错误: {str(e)}")
            finally:
                if os.path.exists(file_path):
                    os.remove(file_path)
    else:
        form = VoiceModelForm()
    return render(request, 'voice_app/train_voice.html', {'form': form})
