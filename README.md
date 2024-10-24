# 语音合成应用

这是一个基于Django的语音合成Web应用程序。该应用允许用户训练语音模型、合成语音，并管理生成的音频文件。

## 功能特点

- 语音模型训练
- 文本到语音合成
- 语音模型列表管理
- 合成音频列表管理
- 用户友好的Web界面

## 技术栈

- Django
- Volcano Engine API (用于语音合成)
- HTML/CSS (前端界面)

## 主要组件

- `voice_app/views/`: 包含所有视图函数
  - `home.py`: 主页视图
  - `train.py`: 语音模型训练视图
  - `synthesize.py`: 语音合成视图
  - `voice_list.py`: 语音模型列表视图
  - `audio_list.py`: 合成音频列表视图

- `voice_app/models/`: 定义数据模型
  - `voice_model.py`: VoiceModel模型
  - `synthesized_audio.py`: SynthesizedAudio模型

## 使用方法

1. 克隆仓库：
   ```
   git clone https://github.com/your-username/voice-synthesis-app.git
   cd voice-synthesis-app
   ```

2. 创建并激活虚拟环境：
   ```
   python -m venv venv
   source venv/bin/activate  # 在Windows上使用 venv\Scripts\activate
   ```

3. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

4. 配置Volcano Engine API密钥：
   - 在项目根目录创建 `.env` 文件
   - 添加以下内容：
     ```
     VOLCANO_ACCESS_KEY=your_access_key
     VOLCANO_SECRET_KEY=your_secret_key
     ```

5. 运行数据库迁移：
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

6. 创建超级用户（可选）：
   ```
   python manage.py createsuperuser
   ```

7. 启动Django开发服务器：
   ```
   python manage.py runserver
   ```

8. 在浏览器中访问 `http://127.0.0.1:8000` 开始使用应用程序

## 贡献

欢迎提交问题报告和拉取请求。

## 许可证

[MIT License](LICENSE)

VOLCANO_ACCESS_KEY=KHxUu33xqaUFA4ejZSOPUtRoh-lxTMlE
VOLCANO_SECRET_KEY=mqJMHneFP5OVgzB4SeyYloMZySkdLLHO
VOLCANO_APPID=8267808772


# 文俊辉
VOLCANO_ACCESS_KEY_WJH=KHxUu33xqaUFA4ejZSOPUtRoh-lxTMlE
VOLCANO_SECRET_KEY_WJH=mqJMHneFP5OVgzB4SeyYloMZySkdLLHO
VOLCANO_APPID_WJH=8267808772

# 张真源
VOLCANO_ACCESS_KEY_ZZY=cJUDbmoujFILXoNNWcUH_uwTTgQlUN63
VOLCANO_SECRET_KEY_ZZY=aPVNov0DysjFAYmNCuaD9GXaUM2Y7ibh
VOLCANO_APPID_ZZY=2839895302


# 王俊凯
VOLCANO_ACCESS_KEY_WJK=-zvLTjoWeUNPv1luykQ6aOqq1DPMYWWE
VOLCANO_SECRET_KEY_WJK=fLnFwvMK8ZML1aNYx2--QBDr44X5-QPg
VOLCANO_APPID_WJK=7230056814

# 孙策-代号鸢
VOLCANO_ACCESS_KEY_SC=WWlKy_cRVDd0awEBqmOz0MXx7sZuLbWO
VOLCANO_SECRET_KEY_SC=hF5-iyz86vzuWTrKFAQ_ZiBgu4aYLRvB
VOLCANO_APPID_SC=8423679321

DJANGO_SECRET_KEY=mqJMHneFP5OVgzB4SeyYloMZySkdLLHO

