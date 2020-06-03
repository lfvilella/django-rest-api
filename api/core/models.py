from django.db import models
from django.contrib.postgres.fields import ArrayField


class Tool(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=250)
    description = models.TextField()
    tags = ArrayField(models.CharField(max_length=200, blank=True))

    def __str__(self):
        return f'{self.title}'
