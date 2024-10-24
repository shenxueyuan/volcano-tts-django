from django.shortcuts import render, redirect
from django.conf import settings
from voice_app.models import VoiceModel
from voice_app.forms import VoiceModelForm
from volcano_engine.train import train_voice_model
import os


def train_voice(request):
    if request.method == 'POST':
        form = VoiceModelForm(request.POST, request.FILES)
        if form.is_valid():
            audio_file = request.FILES['audio_file']
            voice_model = form.cleaned_data['speaker_id']  # 这是一个 VoiceModel 实例
            speaker_id = voice_model.speaker_id  # 获取 speaker_id 字符串
            appid = voice_model.appid
            access_token = voice_model.access_token
            secret_token = voice_model.secret_token

            training_audio_dir = os.path.join(
                settings.MEDIA_ROOT, 'training_audio')
            os.makedirs(training_audio_dir, exist_ok=True)

            file_name = f'{speaker_id}{os.path.splitext(audio_file.name)[1]}'
            file_path = os.path.join(training_audio_dir, file_name)

            with open(file_path, 'wb+') as destination:
                for chunk in audio_file.chunks():
                    destination.write(chunk)

            try:


                response = train_voice_model(
                    access_token,
                    secret_token,
                    file_path,
                    appid,
                    speaker_id  # 使用 speaker_id 字符串而不是 VoiceModel 实例
                )
                if response.get('BaseResp', {}).get('StatusCode') == 0:
                    voice_model.status = VoiceModel.TrainingStatus.AVAILABLE
                    voice_model.save()
                    return redirect('voice_list')
                else:
                    error_message = response.get(
                        'BaseResp', {}).get('StatusMessage', '未知错误')
                    form.add_error(None, f"API 错误: {error_message}")
            except ValueError as e:
                form.add_error(None, f"文件格式错误: {str(e)}")
            except Exception as e:
                form.add_error(None, f"发生错误: {str(e)}")
            finally:
                if os.path.exists(file_path):
                    os.remove(file_path)
    else:
        form = VoiceModelForm()
    return render(request, 'voice_app/train_voice.html', {'form': form})
