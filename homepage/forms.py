from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm
from nocaptcha_recaptcha.fields import NoReCaptchaField
from django.core.exceptions import ValidationError
from schedule.choices import FACULTY_CHOICES, blank_choice_faculty, YEAR_CHOICES, blank_choice_year

class RegistrationForm(UserCreationForm):
    
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Enter your email...',
            'style': 'width: 300px',
        }),
        required=True)

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Enter your first name...',
            'style': 'width: 300px',
        }),
        required=True)
    
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Enter your last name...',
            'style': 'width: 300px',
        }),
        required=True)
    
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
            'style': 'width: 300px',
        }),
        required=True)

    year = forms.ChoiceField(choices= blank_choice_year + YEAR_CHOICES,
        widget=forms.Select( 
            attrs={
                'class':'form-control',
                'style': 'width:300px',
            }),
        required=True)

    captcha = NoReCaptchaField()

    

    class Meta: #Metadata
        model = get_user_model() #Model that is used to submit the data
        fields = (
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'faculty',
            'course_name',
            'year',
        )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Email addresses must be unique.')
        return email

    def save(self, commit=True): #commit means can save to database
        user = super(RegistrationForm, self).save(commit=False) # don't save it yet because not done editing the data for the model
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        
        return user

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'style': 'width:300px',
        }),required=True)
    
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'style':'width:300px',
        }), required=True)

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'style':'width:300px',
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
            'style': 'width: 300px',
        }),
        required=True)

    year = forms.ChoiceField(choices= blank_choice_year + YEAR_CHOICES,
        widget=forms.Select( 
            attrs={
                'class':'form-control',
                'style': 'width:300px',
            }),
        required=True)

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'first_name',
            'last_name',
            'faculty',
            'course_name',
            'year',
            'password',
        )
        #exclude() if only want to exclude a few fields

class CustomAuthenticationForm(AuthenticationForm):
    captcha = NoReCaptchaField()

class EmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not get_user_model().objects.filter(email__iexact=email, is_active=True).exists():
            raise ValidationError("There is no user registered with the specified email address!")

        return email 
        