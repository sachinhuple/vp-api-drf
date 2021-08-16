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


class SongRetrieve(generics.RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'title'

    def get_queryset(self):
        title = self.kwargs.get('title', None)
        queryset = Song.objects.filter(title__iexact=title)
        return queryset

