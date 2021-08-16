from django.shortcuts import render

from django.shortcuts import render
from rest_framework import generics
from .serializers import SongSerializer
from .models import Song
from .pagination import Paginate


class SongsList(generics.ListCreateAPIView):
    serializer_class = SongSerializer
    pagination_class = Paginate

    def get_queryset(self):
        queryset = Song.objects.all()
        return queryset


class SongDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

