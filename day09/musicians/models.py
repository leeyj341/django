from django.db import models

# Create your models here.
# 객체 생성 -> 테이블 명
class Musician(models.Model):
    # 멤버 변수
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    # 인스턴스 호출 시 출력 내용 덮어쓰기(=toString())
    def __str__(self):
        return f'{self.name} : {self.age}'

class Album(models.Model):
    musician = models.ForeignKey(to=Musician, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    release_date = models.DateField()
