from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

menu = [{'title': 'Главная', 'url_n': 'home'},
        {'title': 'Лицей', 'url_n': 'car'},
        ]


# Create your views here.
def index(request):
    return render(request, 'women/index.html', {'menu': menu})


def categories(request, cat_id):
    if cat_id > 2020:
        uri = reverse('home')
        return redirect(uri)
    return HttpResponse(f'Это номер {cat_id}')


def licei(request):
    return HttpResponse('<img src= "https://a.d-cd.net/784c77as-1920.jpg"><h1>Это будущая страница лицея</h1></img>')
