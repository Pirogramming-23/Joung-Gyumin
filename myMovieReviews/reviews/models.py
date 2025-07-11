from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField("제목", max_length=100)
    release_year = models.PositiveIntegerField("개봉년도", null=True, blank=True)  # ✅ 추가
    genre = models.CharField("장르", max_length=50)
    rating = models.FloatField("평점")
    running_time = models.IntegerField("러닝타임(분)", null=True, blank=True)
    content = models.TextField("리뷰 내용")
    director = models.CharField("감독", max_length=100)
    actors = models.CharField("출연진", max_length=100)
    image = models.ImageField("이미지", upload_to='review_images/', null=True, blank=True)

    def __str__(self):
        return self.title