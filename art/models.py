import os

from django.db import models

# Create your models here.

class File(models.Model):

    title = models.CharField(max_length=255, verbose_name='Name')
    photo = models.ImageField(upload_to='pictures/', verbose_name='Painting', default=None, null=True, blank=True)
    file = models.FileField(upload_to='files/', default=None, null=True, blank=True, verbose_name='Files')
    description = models.TextField(default=None, null=True, blank=True)
    href = models.CharField(max_length=255, default=None, null=True, blank=True,  verbose_name='Link')
    code = models.CharField(max_length=255, default=None, null=True, blank=True,  verbose_name='Link to Leetcode')
    easy_tasks_leetcode = models.IntegerField(default=0, blank=True, verbose_name='Easy solved Leetcode problems')
    medium_tasks_leetcode = models.IntegerField(default=0, blank=True, verbose_name='Average solved Leetcode problems')
    hard_tasks_leetcode = models.IntegerField(default=0, blank=True, verbose_name='Complex solved problems Leetcode')

    TYPE_CHOICES = (
        ('picture', 'Painting'),
        ('game', 'A game'),
        ('bot', 'Bot'),
        ('autotest', 'Autotest'),
        ('leetcode', 'Leetcode'),
        ('certificate', 'QA Certificates'),
    )

    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return self.title

    def filename(self):
        return os.path.basename(self.file.name)