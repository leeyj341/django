from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name="followings",
        blank=True
    )
    # 각종 필드를 추가하면
    # createsuperuser가 안 먹으니까 미리 만들어놓든가 
    # admin계정 추가하는 방법 검색해서 적용하기...
    
    # shell_plus에서
    # create_user로 is_staff True, is_superuser True로 줘서 만들어도 됨
