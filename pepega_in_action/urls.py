from django.urls import path

from . import views

urlpatterns = [
    path('', views.memes_list, name='memes_list'),
]