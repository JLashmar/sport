from django.db import models

# Create your models here.

class Country_Data(models.Model):
    name = models.CharField(max_length=250)
    country_slug = models.CharField(max_length=250)
    flag = models.ImageField(blank=True, null=True)

    def __str__(self):
       return self.name
