from django.test import TestCase
from django.urls import reverse
from django.db import models
from django.core.files.uploadedfile import SimpleUploadedFile

import uuid

from schedule.models import SchedulePost
from accounts.models import User
from . import views

# Create your tests here.

class SchedulePostTests(TestCase):
    
    def create_schedule_post(self, id='4a8981e5-cd67-4a16-a388-c3cf3f250d6b', title='Correct Post',faculty='Science', course='Sciences', year=1, semester='1', modules='GER1000', desc='Description'):
        User.objects.create(id=id, email='abc@email.com',faculty=faculty,course_name=course,year=year)
        return SchedulePost.objects.create(user_id=id,title=title, image='', faculty=faculty, course_name=course, year=year, semester=semester, modules_taken=modules, desc=desc)

    def test_post_creation(self):
        post = self.create_schedule_post()
        self.assertTrue(isinstance(post,SchedulePost))
        self.assertEqual(post.__str__(), post.title)
    
    def test_scheduleview_with_no_scheduleposts(self):
        response = self.client.get(reverse('schedule'))

        self.assertEqual(response.status_code, 200)

        self.assertQuerysetEqual(response.context['schedule_posts'],[])

    def test_scheduleview_with_correct_schedulepost(self):

        post = self.create_schedule_post()

        response = self.client.get(reverse('schedule'))

        self.assertQuerysetEqual(
            response.context['schedule_posts'],['<SchedulePost: Correct Post>']
        )
    
    