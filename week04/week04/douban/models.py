from django.db import models

# Create your models here.
class Comment(models.Model):
    mid = models.CharField(max_length=128)
    star = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField()

    class Meta:
        verbose_name = verbose_name_plural = "评论"


class Movie(models.Model):
    mid = models.CharField(primary_key=True, max_length=128)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = verbose_name_plural = "电影"