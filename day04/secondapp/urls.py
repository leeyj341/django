# secondapp/urls.py
from django.urls import path
from . import views
app_name="secondapp"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('static_example/', views.static_example, name="static_example"),
]