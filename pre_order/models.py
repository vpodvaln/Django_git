from django.db import models


class Profile(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
