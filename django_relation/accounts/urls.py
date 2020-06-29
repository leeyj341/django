# accounts의 urls
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('delete/', views.delete, name="delete"),
    path('update/', views.update, name="update"),
    path('password/', views.password, name="password"),
    path('follow/<int:user_pk>/', views.follow, name="follow"),
    # username을 찾는 로직이 사용되는 경우 이 경로가 제일 위에 있으면
    # "login/", "logout/" 같은 경로를 찾을 때 username으로 인식하기 때문에 해당 경로에 접근할 수 없다
    # 그렇기 때문에 제일 아래에 경로를 설정해야 한다.
    path('<str:username>/', views.profile, name="profile"),
]