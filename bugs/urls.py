from django.contrib import admin
from django.urls import path
from .views import show_bugs, bug_description, add_or_edit_bug, add_or_edit_comment

urlpatterns = [
    path('show_bugs/', show_bugs, name="show_bugs"),
    path('<int:pk>/', bug_description, name="bug_description"),
    path('add_bug/', add_or_edit_bug, name="add_bug"),
    path('<int:pk>/edit/', add_or_edit_bug, name="edit_bug"),
    path('<int:pk>/add_comment/', add_or_edit_comment, name="add_comment"),
    path('<int:pk>/edit_comment/', add_or_edit_comment, name="edit_comment"),
]
