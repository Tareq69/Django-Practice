from django.db import models

# Create your models here.

class Musician(models.Model):
    # id = models.AutoField(primary_key = True) automatically created by django
    first_name = models.CharField(max_length = 30)
    last_name  = models.CharField(max_length = 30)
    instrument = models.CharField(max_length = 30)

    def __str__(self):
        return self.first_name + " " + self.last_name
        return self.instrument

class Album(models.Model):
    # id = models.AutoField(primary_key = True) automatically created by django
    artist = models.ForeignKey(Musician, on_delete= models.CASCADE)
    name  = models.CharField(max_length = 30)
    release_date = models.DateField()

    rtp = (
    (1,'waste of time'),
    (2,'Bad'),
    (3,'Average'),
    (4,'Good'),
    (5,'Loved  it'),
    )

    rating = models.IntegerField(choices = rtp)

    def __str__(self):
        # return self.artist
        return self.name
        return self.release_date
        return self.instrument
