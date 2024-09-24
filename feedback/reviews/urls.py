from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view(), name='review'),
    path('thank-you', views.ThankYouView.as_view(), name='thank_you'),
    path('reviews', views.ReviewList.as_view(), name='review_list'),
    path('reviews/favorite', views.AddFavoriteView.as_view(), name='add_favorite'),
    path('reviews/<int:pk>', views.SingleReviewView.as_view(), name='single_review'),
]
