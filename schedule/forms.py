from django import forms
from schedule.models import SchedulePost

class ScheduleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Enter your title',
        }), required=True)
    
    image = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={
            'class':'form-control-file',
            
        }), required=True)

    course_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Enter your course name...',
            'style': 'width:300px',
        }), required=True)

    modules_taken = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter your modules taken here...',
            'style': 'width:300px',
        }), required=True)
    
    desc = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'rows':'10',
            'placeholder':'Enter the schedule description here...'
        }), required=True)

    class Meta:
        model = SchedulePost
        fields = ['title', 'course_name', 'modules_taken', 'desc', 'image']


