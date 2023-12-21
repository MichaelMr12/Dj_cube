from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from women.models import Women

menu = [{'title': 'Главная', 'url_n': 'home'},
        {'title': 'Лицей', 'url_n': 'car'},
        {'title': 'О программе', 'url_n': 'about'},
        ]


# Create your views here.
def index(request):
    return render(request, 'women/index.html', {'menu': menu})


def women_g(request, w_id):
    post = get_object_or_404(Women, pk=w_id)
    return render(request, 'women/women_g.html',  {'menu': menu, 'post':post})

def about(request):
    return render(request, 'women/about.html', {'menu': menu})


def categories(request, cat_id):
    if cat_id > 2020:
        uri = reverse('home')
        return redirect(uri)
    return HttpResponse(f'Это номер {cat_id}')


def licei(request):
    return render(request, 'women/liceum.html', {'menu': menu})
