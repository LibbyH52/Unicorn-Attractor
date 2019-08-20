from django.contrib import admin
from django.urls import path
from .views import get_features, feature_description, new_feature, edit_feature, add_feature_comment, edit_feature_comment, delete_feature_comment

urlpatterns = [
    path('get_features/', get_features, name="get_features"),
    path('<int:pk>/', feature_description, name="feature_description"),
    path('new_feature/', new_feature, name="new_feature"),
    path('<int:pk>/edit_feature/', edit_feature, name="edit_feature"),
    path('<int:pk>/add_feature_comment/', add_feature_comment, name="add_feature_comment"),
    path('<int:pk>/edit_feature_comment/', edit_feature_comment, name="edit_feature_comment"),
    path('<int:pk>/delete_feature_comment/', delete_feature_comment, name="delete_feature_comment"),
]