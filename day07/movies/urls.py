from django.urls import path
from . import views
app_name = "movies"

urlpatterns = [
    path('', views.listMovie, name='list'),
    path('<int:pk>/', views.info, name='info'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),

]