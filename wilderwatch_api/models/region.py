from django.db import models

class Region(models.Model):
    label = models.CharField(max_length=125)
