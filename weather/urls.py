from django.urls import path, include
from . import views


urlpatterns = [
    path('weather', views.index, name='weather'),
]
