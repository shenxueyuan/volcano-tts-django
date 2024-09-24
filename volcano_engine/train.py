import requests
import json
import base64


def train_voice_model(access_key, secret_key, file_path, api_url=None):
    """
    通用的语音模型训练函数

    参数:
    access_key (str): 访问密钥
    secret_key (str): 密钥
    file_path (str): 音频文件的路径
    api_url (str, 可选): API的URL，如果不提供则使用默认值

    返回:
    dict: API的响应
    """
    if api_url is None:
        api_url = "https://open.volcengineapi.com/v2/tts/create_voice"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_key}:{secret_key}"
    }

    with open(file_path, "rb") as audio_file:
        audio_content = audio_file.read()
        audio_base64 = base64.b64encode(audio_content).decode('utf-8')

    payload = {
        "audio_file": audio_base64,
        "audio_format": "m4a",
        "voice_name": "Custom Voice",
        "voice_type": "custom"
    }

    try:
        response = requests.post(
            api_url, headers=headers, data=json.dumps(payload))
        return response.json()
    except requests.RequestException as e:
        return {"code": 5000, "message": f"请求错误: {str(e)}"}


# 示例调用
if __name__ == "__main__":
    pass
