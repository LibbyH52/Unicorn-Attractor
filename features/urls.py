from django.contrib import admin
from django.urls import path
from .views import get_features, new_feature, upvote_feature

urlpatterns = [
    path('get_features/', get_features, name="get_features"),
    path('new_feature/', new_feature, name="new_feature"),
    path('<int:pk>/upvote_feature/', upvote_feature, name="upvote_feature"),
]