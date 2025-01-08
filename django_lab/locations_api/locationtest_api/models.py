from django.db import models

class Location(models.Model):
    street = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
