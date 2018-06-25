from django.shortcuts import render, redirect
from homepage.forms import RegistrationForm

# Create your views here.
def index(request):
    return render(request, 'homepage/home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid: #all the fields are validated
            form.save() #creates user and save data in database
            return redirect('/')
    else: #requesting for the blank form to fill in
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'homepage/reg_form.html', args)
