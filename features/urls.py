from django.contrib import admin
from django.urls import path
from .views import get_features, feature_details

urlpatterns = [
    path('get_features/', get_features, name="get_features"),
    path('feature_details/', feature_details, name="feature_details"),
]