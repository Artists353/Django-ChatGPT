from django.db import models

# Create your models here.

class Artiles(models.Model):
    title = models.CharField("ChatGpt Всех Убьёт", max_length=50)
    announcement = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('ChatGpt написал этот сайт')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
