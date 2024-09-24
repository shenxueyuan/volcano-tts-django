from django import forms
from .models import VoiceModel


class VoiceModelForm(forms.Form):
    name = forms.CharField(max_length=100)
    audio_file = forms.FileField()


class SynthesisForm(forms.Form):
    voice_model = forms.ModelChoiceField(queryset=VoiceModel.objects.all())
    text = forms.CharField(widget=forms.Textarea)
