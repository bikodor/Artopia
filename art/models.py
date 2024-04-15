import os

from django.db import models

# Create your models here.

class File(models.Model):

    title = models.CharField(max_length=255, verbose_name='Название')
    photo = models.ImageField(upload_to='pictures/', verbose_name='Картина', default=None, null=True, blank=True)
    file = models.FileField(upload_to='files/', default=None, null=True, blank=True, verbose_name='Файлы')
    description = models.TextField(default=None, null=True, blank=True)
    href = models.CharField(max_length=255, default=None, null=True, blank=True,  verbose_name='Ссылка')
    code = models.CharField(max_length=255, default=None, null=True, blank=True,  verbose_name='Ссылка на Leetcode')
    easy_tasks_leetcode = models.IntegerField(default=0, blank=True, verbose_name='Легких решённых задач Leetcode')
    medium_tasks_leetcode = models.IntegerField(default=0, blank=True, verbose_name='Средних решённых задач Leetcode')
    hard_tasks_leetcode = models.IntegerField(default=0, blank=True, verbose_name='Сложных решённых задач Leetcode')

    TYPE_CHOICES = (
        ('picture', 'Картина'),
        ('game', 'Игра'),
        ('bot', 'Бот'),
        ('site', 'Сайт'),
        ('autotest', 'Автотест'),
        ('leetcode', 'Leetcode'),
        ('certificate', 'QA Сертификаты'),
    )

    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return self.title

    def filename(self):
        return os.path.basename(self.file.name)