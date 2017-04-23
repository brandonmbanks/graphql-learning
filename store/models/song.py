from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Song(models.Model):

    class Meta:
        db_table = 'songs'

    title = models.CharField(max_length=100)
    artist_id = models.CharField(max_length=50)
    release_date = models.DateField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
