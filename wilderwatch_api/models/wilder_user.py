from django.db import models
from django.contrib.auth.models import User


class WilderUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=1000, blank=True, null=True)
    flair = models.CharField(max_length=150, blank=True, null=True)
    image_url = models.CharField(max_length=600, blank=True, null=True)
    is_researcher = models.BooleanField(default=False)

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
    def username(self):
        return self.user.username