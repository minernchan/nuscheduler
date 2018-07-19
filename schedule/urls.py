from django.urls import path, include
from schedule.views import ScheduleView, ScheduleFormView, schedule_detail,edit_schedule_post, delete_schedule_post, schedule_search
from schedule.models import SchedulePost
from django.views.generic import DetailView

urlpatterns = [
    path('', ScheduleView.as_view(), name='schedule'),
    path('submit/', ScheduleFormView.as_view(), name='schedule_submit'),
    path('<uuid:pk>/', schedule_detail, name='view_schedule'),
    path('edit-schedule/<uuid:pk>/', edit_schedule_post, name='edit_schedule_post'),
    path('delete-schedule/<uuid:pk>/', delete_schedule_post, name='delete_schedule_post'),
    path('search/', schedule_search, name='schedule_search')
]
