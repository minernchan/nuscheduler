from django.shortcuts import render, redirect
from homepage.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash # to make sure user is still logged in after password change
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'homepage/home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid: #all the fields are validated
            form.save() #creates user and save data in database
            return redirect('/register/complete')
    else: #requesting for the blank form to fill in
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'homepage/reg_form.html', args)

def register_complete(request):
    return render(request, 'homepage/reg_done.html')

@login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'homepage/profile.html', args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'homepage/edit_profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/profile')
        else:
            return redirect('/profile/change_password')
    
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'homepage/change_password.html', args)

