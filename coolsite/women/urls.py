from django.urls import path

from women.views import *

urlpatterns = [

    path('', index, name='home'),
    path('liceum/', licei, name= 'car'),
    path('cats/<int:cat_id>/', categories, name='spisok')

]