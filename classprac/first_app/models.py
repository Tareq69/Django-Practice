from django.db import models
from django.urls import reverse

# Create your models here.
class Fighter(models.Model):
    # id = models.AutoField(primary_key = True) automatically created by django
    first_name = models.CharField(max_length = 30)
    last_name  = models.CharField(max_length = 30)
    style = models.CharField(max_length = 30)

    def __str__(self):
        return self.first_name + " " + self.last_name
        return self.instrument
    def get_absolute_url(self):
        return reverse("first_app:fighter_details", kwargs={'pk':self.pk})

class Achievements(models.Model):
    # id = models.AutoField(primary_key = True) automatically created by django
    fighter = models.ForeignKey(Fighter, on_delete= models.CASCADE, related_name='fighter_list')
    name  = models.CharField(max_length = 30)


    def __str__(self):
        return self.name
