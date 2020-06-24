from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail
from django.contrib.auth import get_user_model

# Create your models here.

def articles_image_path(instance, filename):
    return f'user_{instance.user.pk}/{filename}'

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # blank는 유효성 검사 시
    # null은 db 컬럼의 null
    image = models.ImageField(blank=True, upload_to=articles_image_path)
    #upload_to="%y/%m/%d/" 이건 이미지를 날짜 별로 저장하겠다는 의미
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(width=200, height=300)],
        format='JPEG',          # 가장 저용량이면서 화질이 좋음
        options={'quality': 90} # 90은 %
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.pk}번째 글, {self.title} - {self.content}"

class Comment(models.Model):
    article = models.ForeignKey(
        to=Article, 
        on_delete=models.CASCADE)
        # related_name='comments')
    content = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"Article: {self.article}, {self.pk} - {self.content}"

