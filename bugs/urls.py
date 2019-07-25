from django.contrib import admin
from django.urls import path
from .views import show_bugs, bug_description, add_bug, edit_bug, add_comment, edit_comment, delete_comment

urlpatterns = [
    path('show_bugs/', show_bugs, name="show_bugs"),
    path('<int:pk>/', bug_description, name="bug_description"),
    path('add_bug/', add_bug, name="add_bug"),
    path('<int:pk>/edit_bug/', edit_bug, name="edit_bug"),
    path('<int:pk>/add_comment/', add_comment, name="add_comment"),
    path('<int:pk>/edit_comment/', edit_comment, name="edit_comment"),
    path('<int:pk>/delete_comment/', delete_comment, name="delete_comment"),
]
