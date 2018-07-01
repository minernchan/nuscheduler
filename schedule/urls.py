from django.urls import path, include
from schedule.views import ScheduleView, ScheduleFormView
from schedule.models import SchedulePost
from django.views.generic import DetailView

urlpatterns = [
    path('', ScheduleView.as_view(), name='schedule'),
    path('submit/', ScheduleFormView.as_view(), name='schedule_submit'),
    path('<int:pk>/', DetailView.as_view(model=SchedulePost, template_name='schedule/schedule_post.html')),
]
