from django.db import models

# Create your models here.


class DummyGame(models.Model):
    name = models.CharField(max_length=100, default="DummyGame", unique=True)
    description = models.CharField(max_length=2000, default="")
    rating = models.FloatField(null=False, default=0)
