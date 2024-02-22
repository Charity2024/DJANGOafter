from django.shortcuts import render

from django.http import HttpResponse


def karibu(request):
    return HttpResponse("<h1>Welcome to Django class</h1>")


def myhome(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def gallery(request):
    return render(request, 'gallery.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')

# Create your views here.
