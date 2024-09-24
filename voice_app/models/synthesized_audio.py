from django.db import models
from .voice_model import VoiceModel


class SynthesizedAudio(models.Model):
    voice_model = models.ForeignKey(VoiceModel, on_delete=models.CASCADE)
    text = models.TextField()
    audio_file = models.FileField(upload_to='synthesized_audio/')
    created_at = models.DateTimeField(auto_now_add=True)
