from django.urls import path
from . import views
app_name = "articles"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('new/', views.new_write, name="new"),
    path('create/', views.create, name="create"),
    path('introduce/', views.introduce, name="introduce"),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('<int:pk>/edit', views.edit, name="edit"),
    path('<int:pk>/update', views.update, name="update"),
]