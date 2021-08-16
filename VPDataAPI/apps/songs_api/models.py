from django.db import models


class CustomBooleanField(models.BooleanField):

    def from_db_value(self, value, *args, **kwargs):
        if value is None:
            return value
        return int(value)   # return 0/1


class Song(models.Model):
    index = models.BigAutoField(primary_key=True)
    id = models.CharField(max_length=64, unique=True)
    title = models.CharField(max_length=255)
    danceability = models.FloatField()
    energy = models.FloatField()
    key = models.IntegerField()
    loudness = models.FloatField()
    mode = CustomBooleanField()
    acousticness = models.DecimalField(max_digits=50, decimal_places=10)
    instrumentalness = models.DecimalField(max_digits=50, decimal_places=10)
    liveness = models.FloatField()
    valence = models.FloatField()
    tempo = models.FloatField()
    duration_ms = models.IntegerField()
    time_signature = models.IntegerField()
    num_bars = models.IntegerField()
    num_sections = models.IntegerField()
    num_segments = models.IntegerField()
    db_class = models.IntegerField(db_column='class')
    star_rating = models.IntegerField(default=None)


    class Meta:
        db_table = 'song'
