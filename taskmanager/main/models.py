from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    image = models.ImageField('Изображение', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

#TODO: Добавить возможность отправки картинки
#TODO: Прикрутить ML