from django.shortcuts import render


def home(request):
    name = 'Alex'
    return render(request, 'home.html', {'name': name})
