from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Quote(models.Model):
    source = models.CharField(max_length=100, blank=False ,null=False, verbose_name="Источник")
    text = models.TextField(blank=False, null=False, unique=True, verbose_name="Текст цитаты")
    date_added = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0, null=False)
    likes = models.IntegerField(default=0, null=False)
    weight = models.IntegerField(
        default=1,
        verbose_name='Вес',
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    def __str__(self):
        return f'{self.source} | {self.text[:10]}'

