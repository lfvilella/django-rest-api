from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name}'