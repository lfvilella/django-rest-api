from django.db import models


class Tool(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=250)
    description = models.TextField()
    # tags = 

    def __str__(self):
        return f'{self.title}'