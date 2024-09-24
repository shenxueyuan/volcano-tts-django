import os
from pathlib import Path
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# 构建路径,如 BASE_DIR / 'subdir'。
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: 在生产环境中保持密钥的机密性!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

if not SECRET_KEY:
    raise ValueError("未设置 DJANGO_SECRET_KEY 环境变量。请在 .env 文件中设置它。")

# SECURITY WARNING: 不要在生产环境中开启调试模式!
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS',
                          'localhost,127.0.0.1').split(',')

# 应用程序定义
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'voice_app.apps.VoiceAppConfig',  # 使用这个而不是简单的 'voice_app'
]

# 中间件设置
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 模板设置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 数据库设置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 默认主键字段类型
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ... 其他设置 ...

# 静态文件设置
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 媒体文件设置
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 在文件的顶部附近，其他主要设置旁边添加这行
ROOT_URLCONF = 'voice_synthesis_project.urls'

# 火山引擎 API 设置
VOLCANO_ACCESS_KEY = os.getenv('VOLCANO_ACCESS_KEY')
VOLCANO_SECRET_KEY = os.getenv('VOLCANO_SECRET_KEY')

# ... 其他设置 ...
