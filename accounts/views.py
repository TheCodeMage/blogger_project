from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm

#Registration View
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Auto login after register
            messages.success(request, "Registration Successful.")
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

#Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
        
#Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

#Profile View
@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

#Profile Edit View
@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
        else:
            form = UpdateProfileForm(instance=request.user)
        return render(request, 'accounts/edit_profile.html', {'form': form})

    

 

        

