from django.contrib import admin
from django.urls import path
from .views import login, logout, registration


urlpatterns = [
    path('', registration, name="registration"),
    path('accounts/login/', login, name="login"),
    path('logout/', logout, name="logout"),
]