from .views.audio_list import audio_list
from .views.voice_list import voice_list
from .views.synthesize import synthesize_voice
from .views.train import train_voice
from .views.home import home
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


# 如果需要，可以在这里添加任何额外的视图逻辑或辅助函数
