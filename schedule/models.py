import uuid
from django.db import models
from django.contrib.auth import get_user_model

class SchedulePost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=140)
    image = models.ImageField(upload_to='schedule_image')
    faculty = models.CharField(max_length=100)
    course_name = models.CharField(max_length=200)
    year = models.IntegerField()
    semester = models.CharField(max_length=100)
    modules_taken = models.CharField(max_length=500)
    desc = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(get_user_model(),related_name='user_votes')


    def __str__(self):
        return self.title





