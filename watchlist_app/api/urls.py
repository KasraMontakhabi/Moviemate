from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.WatchListGV.as_view(), name="movie_list"),
    path("<int:pk>/", views.WatchDetailAV.as_view(), name="movie_detail"),
    path("stream/", views.StreamPlatformAV.as_view(), name="stream-list"),
    path("stream/<int:pk>/", views.StreamPlatformDetailAV.as_view(),
         name="stream-detail"),
    path("<int:pk>/review-create/",
         views.ReviewCreate.as_view(), name="review-create"),
    path("<int:pk>/reviews/", views.ReviewList.as_view(), name="review-list"),
    path("review/<int:pk>/", views.ReviewDetail.as_view(), name="review-detail"),
    path("reviews/", views.UserReview.as_view(), name="user-review-detail"),
]
