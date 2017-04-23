from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Album(models.Model):

    class Meta:
        db_table = 'albums'

    title = models.CharField(max_length=100)
    artist_id = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    release_date = models.DateField()
