from django.db import models

class StudyType(models.Model):
    label = models.CharField(max_length=125)
