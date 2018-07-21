from django.db import models
from django.contrib.auth import get_user_model
from schedule.models import SchedulePost

class Bookmark(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    bookmarks = models.ManyToManyField(SchedulePost, blank=True, related_name='favourited_schedules')

    def __str__(self):
        return self.user.email