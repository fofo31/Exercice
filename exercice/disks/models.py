from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=200)
    milliseconds = models.IntegerField
    bytes = models.IntegerField
    unitprice = models.DecimalField(max_digits=6, decimal_places=3)
    composer = models.CharField(max_length=200)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
