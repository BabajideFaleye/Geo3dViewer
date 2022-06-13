from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .form import UserRegisterForm

# Create your views here.

@login_required
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = User.objects.create_user(username=username, password=password, email=email)
            # user.save()
            messages.success(request, f'Account has been successfully created for {user}')
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def userAccountCreated(request):
    return render(request, 'users/SuccessfulRegistration.html')
