from django.shortcuts import render


def webdev(request):
    return render(request, 'webdevelopment.html')
