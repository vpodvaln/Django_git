from django.db import models


class Profile(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    # # admin panel view
    # def __str__(self):
    #     return "%s %s" % (self.email, self.name)
    #
    # class Meta:
    #     verbose_name = 'Profile'
    #     verbose_name_plural = 'Profiles'
