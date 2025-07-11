from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100)       # 영화 제목
    year = models.IntegerField()                   # 개봉년도
    genre = models.CharField(max_length=50)        # 장르
    rating = models.FloatField()                   # 별점

    def __str__(self):
        return self.title
