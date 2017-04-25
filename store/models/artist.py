from django.db import models


class Artist(models.Model):

    class Meta:
        db_table = 'artists'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=200)
