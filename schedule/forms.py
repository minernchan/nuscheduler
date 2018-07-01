from django import forms
from schedule.models import SchedulePost

class ScheduleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Enter your title',
        }))

    class Meta:
        model = SchedulePost
        fields = ['title', 'image', 'course_name', 'modules_taken', 'desc']


