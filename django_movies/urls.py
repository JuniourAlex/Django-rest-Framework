from django.urls import path, include
from django_movies.views import  MovieSerialazerView,  MovieSerialazerViewDetail, ReviewCreateView, ReviewALLView,  RatingCreateView

urlpatterns = [
    path('movie/', MovieSerialazerView .as_view()),
    path('movie/<int:pk>/', MovieSerialazerViewDetail.as_view()),
    path('review/create/', ReviewCreateView.as_view()),
    path('review/all/', ReviewALLView.as_view()),
    path('rating/', RatingCreateView.as_view())
]

