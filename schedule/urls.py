from django.urls import path, include
from schedule.views import ScheduleView, ScheduleFormView, edit_schedule_post, delete_schedule_post
from schedule.models import SchedulePost
from django.views.generic import DetailView

urlpatterns = [
    path('', ScheduleView.as_view(), name='schedule'),
    path('submit/', ScheduleFormView.as_view(), name='schedule_submit'),
    path('<int:pk>/', DetailView.as_view(model=SchedulePost, template_name='schedule/schedule_post.html'), name='view_schedule'),
    path('edit-schedule/<int:pk>/', edit_schedule_post, name='edit_schedule_post'),
    path('delete-schedule/<int:pk>/', delete_schedule_post, name='delete_schedule_post'),
]
