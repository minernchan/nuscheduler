from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta: #Metadata
        model = User
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