from schedule.models import SchedulePost
import django_filters
from django import forms
from . import choices

class SchedulePostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Enter keyword...',
            'style': 'width:200px',}
    ))

    faculty = django_filters.ChoiceFilter(choices=choices.FACULTY_CHOICES, widget=forms.Select(
        attrs={
            'class':'form-control',
            'style': 'width:200px',}
    ))

    course_name = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Enter keyword...',
            'style': 'width:200px',}
    ))

    modules_taken = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Enter module code...',
            'style': 'width:200px',}
    ))

    year = django_filters.ChoiceFilter(choices=choices.YEAR_FILTER_CHOICES, widget=forms.Select(
        attrs={
            'class':'form-control',
            'style': 'width:200px',}
    ))

    semester = django_filters.ChoiceFilter(choices=choices.SEMESTER_FILTER_CHOICES, widget=forms.Select(
        attrs={
            'class':'form-control',
            'style': 'width:200px',}
    ))
    
    class Meta:
        model = SchedulePost
        fields = ['title','course_name','modules_taken','year','semester',]


    