from django.contrib import admin
from django.urls import path
from .views import login, logout, registration, user_profile


urlpatterns = [
    path('', registration, name="registration"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('profile/', user_profile, name="profile"),
]