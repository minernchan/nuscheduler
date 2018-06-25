from django.db import models

class SchedulePost(models.Model):
    title = models.CharField(max_length=140)
    image = models.ImageField()
    desc = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title