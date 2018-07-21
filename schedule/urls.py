from django.urls import path, include
from . import views
from schedule.models import SchedulePost
from django.views.generic import DetailView

urlpatterns = [
    path('', views.ScheduleView.as_view(), name='schedule'),
    path('submit/', views.ScheduleFormView.as_view(), name='schedule_submit'),
    path('<uuid:pk>/', views.schedule_detail, name='view_schedule'),
    path('edit-schedule/<uuid:pk>/', views.edit_schedule_post, name='edit_schedule_post'),
    path('delete-schedule/<uuid:pk>/', views.delete_schedule_post, name='delete_schedule_post'),
    path('search/', views.schedule_search, name='schedule_search'),
    path('like-schedule/<uuid:pk>/', views.like_schedule, name='like_schedule'),
    path('remove-like-schedule/<uuid:pk>/', views.remove_like_schedule, name='remove_like_schedule'),

]
