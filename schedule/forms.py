from django import forms

from multiselectfield import MultiSelectFormField
from django_select2.forms import Select2MultipleWidget, HeavySelect2MultipleWidget
from pagedown.widgets import PagedownWidget

from schedule.models import SchedulePost
from schedule.choices import FACULTY_CHOICES, blank_choice_faculty, blank_choice_year, YEAR_CHOICES_SCHEDULE, blank_choice_semester, SEMESTER_CHOICES, MODULE_CHOICES

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

    faculty = forms.ChoiceField(choices= blank_choice_faculty + FACULTY_CHOICES,
        widget=forms.Select( 
            attrs={
                'class':'form-control',
                'style': 'width:300px',
            }),
        required=True)

    course_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Enter your course name...',
            'style': 'width:300px',
        }), required=True)

    year = forms.ChoiceField(choices= blank_choice_year + YEAR_CHOICES_SCHEDULE,
        widget=forms.Select( 
            attrs={
                'class':'form-control',
                'style': 'width:300px',
            }),
        required=True)

    semester = forms.ChoiceField(choices= blank_choice_semester + SEMESTER_CHOICES,
        widget=forms.Select( 
            attrs={
                'class':'form-control',
                'style': 'width:300px',
            }),
        required=True)

    #modules_taken = forms.CharField(widget=forms.TextInput(
    #    attrs={
    #        'class':'form-control',
    #        'placeholder':'Enter your modules taken here...',
    #        'style': 'width:300px',
    #    }), required=True)
    
    modules_taken = forms.MultipleChoiceField(choices=MODULE_CHOICES, 
        widget=Select2MultipleWidget(attrs={
                'class':'form-control',
                'style': 'width:300px;',
                'data-placeholder': 'Please enter your modules taken here...'
            }))


    desc = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'rows':'10',
            'placeholder':'Enter the schedule description here...'
        }), required=True)

    class Meta:
        model = SchedulePost
        fields = ['title', 'image','faculty', 'course_name', 'year', 'semester', 'modules_taken', 'desc',]


