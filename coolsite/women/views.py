from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

menu = [{'title': 'Главная', 'url_n': 'home'},
        {'title': 'Лицей', 'url_n': 'car'},
        {'title': 'О программе', 'url_n': 'about'},
        ]


# Create your views here.
def index(request):
    return render(request, 'women/index.html', {'menu': menu})


def about(request):
    return render(request, 'women/about.html', {'menu': menu})


def categories(request, cat_id):
    if cat_id > 2020:
        uri = reverse('home')
        return redirect(uri)
    return HttpResponse(f'Это номер {cat_id}')


def licei(request):
    return render(request, 'women/liceum.html', {'menu': menu})
