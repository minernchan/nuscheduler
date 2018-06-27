from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm
from nocaptcha_recaptcha.fields import NoReCaptchaField
from django.core.exceptions import ValidationError

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    captcha = NoReCaptchaField()

    class Meta: #Metadata
        model = User #Model that is used to submit the data
        fields = (
            'username', 
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )
    
    def save(self, commit=True): #commit means can save to database
        user = super(RegistrationForm, self).save(commit=False) # don't save it yet because not done editing the data for the model
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        
        return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )
        #exclude() if only want to exclude a few fields

class CustomAuthenticationForm(AuthenticationForm):
    captcha = NoReCaptchaField()

class EmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise ValidationError("There is no user registered with the specified email address!")

        return email 
        