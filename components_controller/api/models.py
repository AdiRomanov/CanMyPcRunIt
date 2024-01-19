from django.db import models


# Create your models here.

class CpuScore(models.Model):
    manufacturer = models.CharField(max_length=1500, default='DefaultName')
    model = models.CharField(max_length=1500, default='DefaultNameM')
    score = models.FloatField(null=True, blank=True)


class Game(models.Model):
    """
    Această clasă definește modelul pentru jocuri în cadrul aplicației.
    """
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
        """
        Metodă care returnează reprezentarea șir a obiectului Game, utilizată pentru afișare în administrarea Django.
        """
        return self.name
