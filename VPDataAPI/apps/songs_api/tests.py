from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Song
from rest_framework import status
from django.urls import reverse

# using DRF provided APITestCase
class StudentAPITestCase(APITestCase):
    print("Testing song api using drf TestCase")
    header = {}

    def setUp(self):
        Song.objects.create(
              id="3kOtrXdDW7zkcLP5IrMmDctest",
              title="This is test title",
              danceability=0.864,
              energy=0.255,
              key=0,
              loudness=-9.333,
              mode=True,
              acousticness="0.6420000000",
              instrumentalness="0.0156000000",
              liveness=0.114,
              valence=0.495,
              tempo=87.944,
              duration_ms=194163,
              time_signature=4,
              num_bars=70,
              num_sections=8,
              num_segments=688,
              db_class=1,
              star_rating=3
            )

    def test_get_details_method(self):
        response = self.client.get('/api/v1/song-api/song/1/', {}, Headers=self.header, secure=True)
        self.assertEqual(response.status_code, 200)

    def test_get_list_method(self):

        response = self.client.get('/api/v1/song-api/song/?p=1', {}, Headers=self.header, secure=True)
        self.assertEqual(response.status_code, 200)
        qs = Song.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_post_method(self):
        response = self.client.post(
            path='/api/v1/song-api/song/',
            data={
                    "id": "3kOtrXdDW7zkcLP5IrMmDc",
                    "title": "By The Shore",
                    "danceability": 0.834,
                    "energy": 0.256,
                    "key": 0,
                    "loudness": -9.433,
                    "mode": False,
                    "acousticness": "0.6420000000",
                    "instrumentalness": "0.0156000000",
                    "liveness": 0.104,
                    "valence": 0.496,
                    "tempo": 88.944,
                    "duration_ms": 194164,
                    "time_signature": 4,
                    "num_bars": 71,
                    "num_sections": 9,
                    "num_segments": 687,
                    "db_class": 1,
                    "star_rating": 4
            },
            Headers=self.header,
            secure=True,
            format='json'
        )

        self.assertEqual(response.status_code, 201)
        qs = Song.objects.all()
        self.assertEqual(qs.count(), 2)

    def test_put_method(self):
        response = self.client.put(
            path='/api/v1/song-api/song/1/',
            data={
                    "id": "3kOtrXdDW7zkcLP5IrMmDctest",
                    "title": "test title 2",
                    "danceability": 0.834,
                    "energy": 0.256,
                    "key": 0,
                    "loudness": -9.433,
                    "mode": False,
                    "acousticness": "0.6420000000",
                    "instrumentalness": "0.0156000000",
                    "liveness": 0.104,
                    "valence": 0.496,
                    "tempo": 88.944,
                    "duration_ms": 194164,
                    "time_signature": 4,
                    "num_bars": 71,
                    "num_sections": 9,
                    "num_segments": 687,
                    "db_class": 1,
                    "star_rating": 5
            },
            Headers=self.header,
            secure=True,
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        qs = Song.objects.get(index=1)
        self.assertEqual(qs.title, "test title 2")

    def test_patch_method(self):
        response = self.client.patch(
            path='/api/v1/song-api/song/1/',
            data={"title": "This is test title"},
            Headers=self.header,
            secure=True,
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        qs = Song.objects.get(index=1)
        self.assertEqual(qs.title, "This is test title")

    def test_delete_method(self):
        response = self.client.delete(
            path='/api/v1/song-api/song/1/',
            data={},
            Headers=self.header,
            secure=True,
            format='json'
        )
        print(" response ", response)
        self.assertEqual(response.status_code, 204)
        qs = Song.objects.all()
        self.assertEqual(qs.count(), 0)



