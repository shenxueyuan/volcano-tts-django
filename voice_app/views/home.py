from django.shortcuts import render


def home(request):
    return render(request, 'voice_app/home.html')
