"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('hello/', views.hello),
    path('name/', views.name),
    path('introduce/', views.introduce),
    path('randompick/', views.pickStudent),
    path('yourname/<str:name>', views.yourname),
    path('info/<str:name>/<int:age>', views.info),
    path('multiple/<int:num1>/<int:num2>', views.multiple),
    path('gugu/<int:num1>/<int:num2>', views.gugu),
    path('pigeon/<int:big>/<int:small>', views.pigeon),
    path('dtl/', views.dtl),
    path('forif/<str:my_str>', views.forif),
]
