from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    tools = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    link = models.URLField(max_length=5000)


class Achievement(models.Model):
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=5000)
    link = models.URLField(max_length=5000)
    rank = models.CharField(max_length=50, blank=True)


class Certification(models.Model):
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=5000)
    link = models.URLField(max_length=5000)