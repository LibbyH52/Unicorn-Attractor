from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import login, logout, registration, user_profile


urlpatterns = [
    path('', registration, name="registration"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('profile/', user_profile, name="profile"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]