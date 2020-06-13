# pages/urls.py

from django.urls import path
from . import views
app_name="pages"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('loop/', views.loop, name="loop"),
    path('throw/', views.throw, name="throw"),
    path('catch/', views.catch, name="catch"),
    path('food/<str:name>', views.food, name="food"),
    path('getCount/', views.getCount, name="getCount"),
    path('lotto/', views.lotto, name="lotto"),
    path('artii/', views.artii, name="artii"),
    path('result/', views.result, name="result"),
]