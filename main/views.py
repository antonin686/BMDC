from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html', {'title': 'Main - home'})
