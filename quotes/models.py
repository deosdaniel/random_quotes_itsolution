from django.db import models

# Create your models here.

class Quote(models.Model):
    source = models.CharField(max_length=100, blank=False ,null=False)
    text = models.TextField(blank=False, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0, null=False)
    likes = models.IntegerField(default=0, null=False)

    def __str__(self):
        return f'{self.source} | {self.text[:10]}'

    #weight = models.IntegerField(default=0)