from django.urls import path, include
from django.views.generic import ListView, DetailView
from update.models import UpdatePost

urlpatterns = [
    path('', ListView.as_view(queryset=UpdatePost.objects.all().order_by("-date")[:25], template_name="update/update.html"), name='updates'),
    path('<uuid:pk>/', DetailView.as_view(model=UpdatePost, template_name='update/post.html'))
]