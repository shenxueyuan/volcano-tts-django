from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
from django.conf import settings
from voice_app.models import SynthesizedAudio
from voice_app.forms import SynthesisForm
from volcano_engine.synthesize import synthesize_speech
import uuid


def synthesize_voice(request):
    if request.method == 'POST':
        form = SynthesisForm(request.POST)
        if form.is_valid():
            voice_model = form.cleaned_data['voice_model']
            text = form.cleaned_data['text']

            response = synthesize_speech(
                settings.VOLCANO_ACCESS_KEY,
                settings.VOLCANO_SECRET_KEY,
                text,
                voice_model.speaker_id
            )

            if response['code'] == 3000:
                audio_data = response['data']
                synthesized_audio = SynthesizedAudio(
                    voice_model=voice_model, text=text)
                synthesized_audio.audio_file.save(
                    f'{uuid.uuid4()}.mp3', ContentFile(audio_data))
                return redirect('audio_list')
    else:
        form = SynthesisForm()
    return render(request, 'voice_app/synthesize_voice.html', {'form': form})
