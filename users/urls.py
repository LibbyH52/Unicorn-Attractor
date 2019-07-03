from django.contrib import admin
from django.urls import path
from .views import registration, login, logout


urlpatterns = [
    path('registration/', registration, name="registration"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
]