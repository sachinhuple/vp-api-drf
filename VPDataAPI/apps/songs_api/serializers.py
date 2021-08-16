from rest_framework import serializers
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Song


# Serializer to serialize song data
class SongSerializer(serializers.ModelSerializer):
    star_rating = serializers.IntegerField(required=False, min_value=1, max_value=5)

    class Meta:
        model = Song
        fields = ['index', 'id', 'title', 'danceability', 'energy', 'key', 'loudness', 'mode', 'acousticness',
                  'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature',
                  'num_bars', 'num_sections', 'num_segments', 'db_class', 'star_rating']
        # fields = '__all__'

        # validators = [MinValueValidator(1), MaxValueValidator(5)]
