from django.db import models


# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=1500, default='DefaultName')
    description = models.TextField(null=True, blank=True)
    developer = models.CharField(max_length=1500, null=True, blank=True)

    ram_min = models.FloatField(null=True, blank=True)
    cpu_min = models.CharField(max_length=1500, null=True, blank=True)
    gpu_min = models.CharField(max_length=1500, null=True, blank=True)
    OS_min = models.CharField(max_length=1500, null=True, blank=True)
    storage_min = models.FloatField(null=True, blank=True)

    ram_rec = models.FloatField(null=True, blank=True)
    cpu_rec = models.CharField(max_length=1500, null=True, blank=True)
    gpu_rec = models.CharField(max_length=1500, null=True, blank=True)
    OS_rec = models.CharField(max_length=1500, null=True, blank=True)
    storage_rec = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

