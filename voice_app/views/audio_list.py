from django.shortcuts import render
from voice_app.models import SynthesizedAudio


def audio_list(request):
    audios = SynthesizedAudio.objects.all()
    return render(request, 'voice_app/audio_list.html', {'audios': audios})
