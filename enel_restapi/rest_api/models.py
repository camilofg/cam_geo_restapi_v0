from django.db import models
from django.utils import timezone


class Item(models.Model):
    description = models.CharField(max_length=100, null=True)
    creation_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.description


class Element(models.Model):
    description = models.CharField(max_length=100, null=True)
    serial = models.CharField(max_length=50)

    def __str__(self):
        return self.description

