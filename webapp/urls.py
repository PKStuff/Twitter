from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tweet/',views.twitter, name='tweet'),
    path('<int:tweet_id>/',views.favorite, name='favorite')
]