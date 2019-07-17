from django.contrib import admin
from django.urls import path
from .views import get_features

urlpatterns = [
    path('get_features/', get_features, name="get_features"),
]