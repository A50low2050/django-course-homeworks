from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена')
    image = models.URLField(verbose_name='Изображение')
    release_date = models.DateTimeField(verbose_name='Дата выхода')
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=50, verbose_name='Слаг')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
