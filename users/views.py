from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    """ render a user creation form and handle submission """

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for: {username}, you can now login!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


# Can also set this variable in the projects settings.py
@login_required(login_url='login')
def profile(request):
    """ Load the users profile """
    return render(request, 'users/profile.html')
