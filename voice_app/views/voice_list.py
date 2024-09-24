from django.shortcuts import render
from voice_app.models import VoiceModel


def voice_list(request):
    voices = VoiceModel.objects.all()
    return render(request, 'voice_app/voice_list.html', {'voices': voices})
