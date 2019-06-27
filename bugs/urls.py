from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_bugs, name="show_bugs"),
    path('<int:pk>/', views.bug_description, name="bug_description"),
]