from django import forms
from django.conf import settings
from .models import VoiceModel


class VoiceModelForm(forms.ModelForm):
    speaker_id = forms.ModelChoiceField(
        queryset=VoiceModel.objects.all(),
        label='选择音色',
        to_field_name='speaker_id'
    )

    class Meta:
        model = VoiceModel
        fields = ['speaker_id']  # 移除 'name' 字段

    audio_file = forms.FileField(label='音频文件')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['speaker_id'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['audio_file'].widget.attrs.update(
            {'class': 'form-control'})


class SynthesisForm(forms.Form):
    voice_model = forms.ModelChoiceField(
        queryset=VoiceModel.objects.filter(
            status=VoiceModel.TrainingStatus.AVAILABLE),
        label='选择音色',
        empty_label=None
    )
    text = forms.CharField(widget=forms.Textarea, label='要合成的文本')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['voice_model'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
