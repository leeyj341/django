from django.db import models

# Create your models here.
class Article(models.Model) : # articles_article
    title = models.CharField(max_length=150)                # 글자수를 제한하고 싶을 때 사용
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    # 자동으로 처음 생성된 시간을 넣어주겠다
    updated_at = models.DateTimeField(auto_now=True)        # 글이 생성(=수정)되는 시간을 넣어주겠다
    # boolean - models.BooleanField(blank=True)

    # 매직 메서드 java의 toString()과 같은 역할 
    def __str__(self) :
        return f'{self.id}번째 글 - {self.title} : {self.content}'