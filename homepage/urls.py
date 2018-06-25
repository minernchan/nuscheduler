from django.urls import path, include
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', login, {'template_name': 'homepage/login.html'}),
    path('logout/', logout, {'template_name': 'homepage/logout.html'}),
    path('register/', views.register, name='register'),
]
