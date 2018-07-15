from django.urls import path, include
from . import views
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
    )
from homepage.forms import CustomAuthenticationForm, EmailValidationOnForgotPassword

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', login, {'template_name': 'homepage/login.html', 'authentication_form': CustomAuthenticationForm}),
    path('logout/', logout, {'template_name': 'homepage/logout.html'}),
    path('register/', views.register, name='register'),
    path('register/complete/', views.register_complete, name='register_complete'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/view/<id>/', views.view_other_profile, name='view_other_profile'),
    path('profile/view/<id>/uploaded-schedules', views.view_uploaded_schedules, name='view_uploaded_schedules'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/password/', views.change_password, name='change_password'),
    path('reset-password/', password_reset, 
    {'template_name': 'homepage/reset_password.html', 'email_template_name': 'homepage/reset_password_email.html',
     'password_reset_form': EmailValidationOnForgotPassword}, name='reset_password'),
    path('reset-password/done/', password_reset_done, {'template_name': 'homepage/reset_password_done.html'}, name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', password_reset_confirm, {'template_name': 'homepage/reset_password_confirm.html'}, name='password_reset_confirm'),
    path('reset-password/complete/', password_reset_complete, {'template_name': 'homepage/reset_password_complete.html'}, name='password_reset_complete')
]
