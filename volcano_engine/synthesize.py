import requests
import json


def synthesize_speech(access_key, secret_key, text, speaker_id, api_url=None):
    """
    通用的语音合成函数

    参数:
    access_key (str): 访问密钥
    secret_key (str): 密钥
    text (str): 要合成的文本
    speaker_id (str): 说话人ID
    api_url (str, 可选): API的URL，如果不提供则使用默认值

    返回:
    dict: 包含合成音频数据的响应
    """
    if api_url is None:
        api_url = "https://open.volcengineapi.com/v2/tts/synthesize"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_key}:{secret_key}"
    }

    payload = {
        "text": text,
        "voice_id": speaker_id,
        "audio_format": "mp3",
        "sample_rate": 16000
    }

    try:
        response = requests.post(
            api_url, headers=headers, data=json.dumps(payload))
        return response.json()
    except requests.RequestException as e:
        return {"code": 5000, "message": f"请求错误: {str(e)}"}


def save_audio_file(audio_data, file_path):
    """
    保存音频文件

    参数:
    audio_data (bytes): 音频数据
    file_path (str): 保存文件的路径

    返回:
    bool: 保存是否成功
    """
    try:
        with open(file_path, 'wb') as f:
            f.write(audio_data)
        return True
    except IOError as e:
        print(f"保存音频文件时出错: {str(e)}")
        return False
