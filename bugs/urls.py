from django.contrib import admin
from django.urls import path
from .views import show_bugs, bug_description, add_bug

urlpatterns = [
    path('show_bugs', show_bugs, name="show_bugs"),
    path('<int:pk>/', bug_description, name="bug_description"),
    path('add_bug/', add_bug, name="add_bug"),
]