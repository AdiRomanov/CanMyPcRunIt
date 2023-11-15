from django.db import models


# Create your models here.


class DummyGame(models.Model):
    name = models.CharField(max_length=100, default="DummyGame", unique=True)
    description = models.CharField(max_length=2000, default="")
    rating = models.FloatField(null=False, default=0)


class Info(models.Model):
    description = models.TextField()
    developer = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MinimumRequirements(models.Model):
    OS_min = models.CharField(max_length=255)
    cpu_min = models.CharField(max_length=255)
    gpu_min = models.CharField(max_length=255)
    ram_min = models.IntegerField()
    storage_min = models.FloatField()


class RecommendedRequirements(models.Model):
    OS_rec = models.CharField(max_length=255, null=True, blank=True)
    cpu_rec = models.CharField(max_length=255, null=True, blank=True)
    gpu_rec = models.CharField(max_length=255, null=True, blank=True)
    ram_rec = models.IntegerField(null=True, blank=True)
    storage_rec = models.FloatField(null=True, blank=True)


"""class Game(models.Model):
    info = models.OneToOneField(Info, on_delete=models.CASCADE)
    minimum_requirements = models.OneToOneField(MinimumRequirements, on_delete=models.CASCADE)
    recommended_requirements = models.OneToOneField(RecommendedRequirements, on_delete=models.CASCADE)

    def __str__(self):
        return self.info.name
"""


class Game(models.Model):
    info = models.JSONField()
    minimum_requirements = models.JSONField()
    recommended_requirements = models.JSONField()

    def __str__(self):
        return self.info.get('name', 'Game')
