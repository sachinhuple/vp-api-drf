from django.urls import path
from . import views


urlpatterns = [
    path('song/', views.SongsList.as_view()),
    path('song/<int:pk>/', views.SongDetails.as_view()),
]