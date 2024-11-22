from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена')
    image = models.CharField(max_length=100, verbose_name='Изображение')
    release_date = models.DateField(verbose_name='Дата релиза')
    lte_exists = models.BooleanField(default=False, verbose_name='Налитие LTE')
    slug = models.CharField(max_length=70)
    
    
