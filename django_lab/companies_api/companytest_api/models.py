from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=32)
    industry = models.CharField(max_length=32)