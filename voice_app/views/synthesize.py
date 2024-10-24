from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
from django.conf import settings
from voice_app.models import SynthesizedAudio
from voice_app.forms import SynthesisForm
from volcano_engine.synthesize import synthesize_speech
import uuid
import base64
import os

os.environ['PYTHONIOENCODING'] = 'utf-8'


def synthesize_voice(request):
    if request.method == 'POST':
        form = SynthesisForm(request.POST)
        if form.is_valid():
            voice_model = form.cleaned_data['voice_model']
            text = form.cleaned_data['text']

            # 生成唯一的用户ID（这里使用UUID作为示例）
            user_id = str(uuid.uuid4())

            # 生成 access_token
            access_token = settings.VOLCANO_ACCESS_KEY

            response = synthesize_speech(
                voice_model.access_token,
                voice_model.secret_token,
                text,
                voice_model.speaker_id,
                voice_model.appid,
                access_token,
                user_id
            )

            if response.get('code') == 3000:  # 成功状态码为 3000
                audio_data = base64.b64decode(response.get('data', ''))
                if audio_data:
                    synthesized_audio = SynthesizedAudio(
                        voice_model=voice_model, text=text[:10])
                    synthesized_audio.audio_file.save(
                        f'{uuid.uuid4()}.mp3', ContentFile(audio_data))

                    # 可以选择保存或使用其他元数据
                    duration = response.get('addition', {}).get('duration')
                    if duration:
                        synthesized_audio.duration = int(duration)
                    synthesized_audio.save()

                    return redirect('audio_list')
                else:
                    form.add_error(None, "未能获取音频数据")
            else:
                error_message = response.get('message', '未知错误')
                form.add_error(None, f"API 错误: {error_message}")
    else:
        form = SynthesisForm()
    return render(request, 'voice_app/synthesize_voice.html', {'form': form})
