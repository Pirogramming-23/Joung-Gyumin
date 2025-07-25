# Generated by Django 5.2.4 on 2025-07-11 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('release_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='개봉년도')),
                ('genre', models.CharField(max_length=50, verbose_name='장르')),
                ('rating', models.FloatField(verbose_name='평점')),
                ('running_time', models.IntegerField(blank=True, null=True, verbose_name='러닝타임(분)')),
                ('content', models.TextField(verbose_name='리뷰 내용')),
                ('director', models.CharField(max_length=100, verbose_name='감독')),
                ('actors', models.CharField(max_length=100, verbose_name='출연진')),
                ('image', models.ImageField(blank=True, null=True, upload_to='review_images/', verbose_name='이미지')),
            ],
        ),
    ]
