from django.urls import path
from . import views

app_name = "musicians"

urlpatterns=[
    # u - v - t 순서 고정.
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    # django가 지정한 경로 작성 방식
    # <데이터 타입 : 변수 명>
    # 실제 사용자가 작성하는 url
    path('<int:musician_pk>/', views.detail, name="detail"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/edit/', views.edit, name="edit"),
    path('<int:musician_pk>/create_album/', views.create_album, name="create_album"),
    path('<int:musician_pk>/delete_album/<int:album_pk>/', views.delete_album, name="delete_album"),
]