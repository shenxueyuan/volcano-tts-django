import requests
import json
import base64
import uuid
import mimetypes


def train_voice_model(access_key, secret_key, file_path, appid, speaker_id, api_url=None):
    """
    通用的语音模型训练函数

    参数:
    access_key (str): 访问密钥
    secret_key (str): 密钥
    file_path (str): 音频文件的路径
    appid (str): 应用ID
    speaker_id (str): 说话人ID
    api_url (str, 可选): API的URL，如果不提供则使用默认值

    返回:
    dict: API的响应
    """
    if api_url is None:
        api_url = "https://openspeech.bytedance.com/api/v1/mega_tts/audio/upload"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer;{access_key}",
        "Resource-Id": "volc.megatts.voiceclone"
    }

    # 获取文件的 MIME 类型
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type:
        # 根据 MIME 类型映射到目标格式
        mime_to_format = {
            'audio/wav': 'wav',
            'audio/x-wav': 'wav',
            'audio/mpeg': 'mp3',
            'audio/mp3': 'mp3',
            'audio/ogg': 'ogg',
            'audio/x-m4a': 'm4a',
            'audio/aac': 'aac',
            'audio/x-aac': 'aac',
            'audio/x-pcm': 'pcm',
            'audio/mp4a-latm': 'm4a'
        }
        audio_format = mime_to_format.get(mime_type, mime_type.split('/')[-1])
        if audio_format not in ['wav', 'mp3', 'ogg', 'm4a', 'aac', 'pcm']:
            raise ValueError(f"不支持的音频格式：{audio_format}")
    else:
        raise ValueError("无法确定音频文件格式")

    with open(file_path, "rb") as audio_file:
        audio_content = audio_file.read()
        audio_base64 = base64.b64encode(audio_content).decode('utf-8')

    payload = {
        "appid": appid,
        "speaker_id": speaker_id,
        "audios": [{
            "audio_bytes": audio_base64,
            "audio_format": audio_format
        }],
        "source": 2,
        "language": 0,  # 0 表示中文，根据需要调整
        "model_type": 1  # 使用 2.0 效果
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        return response.json()
    except requests.RequestException as e:
        return {"BaseResp": {"StatusCode": 5000, "StatusMessage": f"请求错误: {str(e)}"}}


# 示例调用
if __name__ == "__main__":
    pass
