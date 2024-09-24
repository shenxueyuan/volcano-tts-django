from django.db import models


class VoiceModel(models.Model):
    name = models.CharField(max_length=100)
    speaker_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
