from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    published_date = models.DateTimeField(null=True, blank=True, verbose_name="Дата публикации")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-created_date']
