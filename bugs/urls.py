from django.contrib import admin
from django.urls import path
from .views import show_bugs, bug_description, add_bug, edit_bug, add_bug_comment, edit_bug_comment, delete_bug_comment

urlpatterns = [
    path('show_bugs/', show_bugs, name="show_bugs"),
    path('<int:pk>/', bug_description, name="bug_description"),
    path('add_bug/', add_bug, name="add_bug"),
    path('<int:pk>/edit_bug/', edit_bug, name="edit_bug"),
    path('<int:pk>/add_bug_comment/', add_bug_comment, name="add_bug_comment"),
    path('<int:pk>/edit_bug_comment/', edit_bug_comment, name="edit_bug_comment"),
    path('<int:pk>/delete_bug_comment/', delete_comment, name="delete_bug_comment"),
]
