from django.urls import path
from .views import WhatchlistListAV, WatchlistDetailAV, StreamPlatformListAV, StreamPlatformDetailAV

urlpatterns = [
    path('list', WhatchlistListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchlistDetailAV.as_view(), name='movie-detail'),
    path('stream', StreamPlatformListAV.as_view(), name='streamplatform-list'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-detail')
]
