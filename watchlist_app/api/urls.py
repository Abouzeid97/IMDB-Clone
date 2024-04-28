from django.urls import path
from .views import (WhatchlistListAV, WatchlistDetailAV, StreamPlatformListAV,
                    StreamPlatformDetailAV, ReviewListGAV, ReviewDetailGAV,
                    ReviewCreate, UserReview)

urlpatterns = [
    path('list/', WhatchlistListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchlistDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformListAV.as_view(), name='streamplatform-list'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    path('<int:pk>/review-create/',ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/review/', ReviewListGAV.as_view(), name='reviewlist'),
    path('review/<int:pk>/', ReviewDetailGAV.as_view(), name='review-detail'),
    path('review/<str:username>', UserReview.as_view(), name='user'),
#         stream/<int:pk>/review/<int:pk>    
]
