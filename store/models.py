from django.db import models
from django.urls import reverse



class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    price = models.IntegerField(verbose_name='Цена')
    photo = models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name="Фото")
    description = models.TextField(default=None, null=True)
    # category = models.ForeignKey('Category', blank=True, on_delete=models.PROTECT, related_name='cat')
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    time_create = models.DateTimeField(
        auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('store:product', kwargs={'slug': self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cats', kwargs={'cat_slug': self.slug})

class Basket(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    price = models.IntegerField(verbose_name='Цена')
    photo = models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name="Фото")
    count = models.IntegerField(verbose_name="Количество", default=1)

    def __str__(self):
        return self.title

