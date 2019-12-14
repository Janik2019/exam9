from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    photo = models.ImageField(upload_to='photos', verbose_name='Фото')
    signature = models.CharField(max_length=200, verbose_name='Подпись')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    author = models.ForeignKey(User, related_name='photos', on_delete=models.CASCADE, verbose_name='Автор')
    like = models.ManyToManyField(User, through='webapp.Like', blank=True, verbose_name='userslike')

    def __str__(self):
        return self.signature


class Comment(models.Model):
    descr = models.TextField(max_length=1000, verbose_name='Текст')
    photo = models.ForeignKey('webapp.Photo', related_name='photo_comments', on_delete=models.CASCADE, verbose_name='Фотография')
    author = models.ForeignKey(User, related_name='author_comments', on_delete=models.CASCADE, verbose_name='Автор')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.descr


class Like(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, null=True, blank=True, verbose_name='photo', related_name='photolikes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='author', related_name='userlikes')
