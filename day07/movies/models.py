from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300)
    audience = models.IntegerField()
    open_date = models.DateField()
    genre = models.CharField(max_length=300)
    watch_grade = models.CharField(max_length=300)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

    def __str__(self) :
        return f"{self.title} : {self.title_en} : {self.audience} : {self.open_date} : {self.genre} : {self.watch_grade} : {self.score} : {self.poster_url} : {self.description}"
