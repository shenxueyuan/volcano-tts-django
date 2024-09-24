from django.urls import path
from .views import home, train_voice, synthesize_voice, voice_list, audio_list

urlpatterns = [
    path('', home, name='home'),
    path('train/', train_voice, name='train_voice'),
    path('synthesize/', synthesize_voice, name='synthesize_voice'),
    path('voices/', voice_list, name='voice_list'),
    path('audios/', audio_list, name='audio_list'),
]
