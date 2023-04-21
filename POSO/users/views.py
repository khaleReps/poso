from django.shortcuts import render


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from users.forms import EmailLoginSettingsForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your password was successfully updated!')
            return redirect('users:profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})


@login_required
def profile(request):
    # Get the user's email login settings
    email_host = request.user.email_host
    email_port = request.user.email_port
    email_use_ssl = request.user.email_use_ssl

    if request.method == 'POST':
        # Update the user's email login settings
        form = EmailLoginSettingsForm(request.POST)
        if form.is_valid():
            request.user.email_host = form.cleaned_data['email_host']
            request.user.email_port = form.cleaned_data['email_port']
            request.user.email_use_ssl = form.cleaned_data['email_use_ssl']
            request.user.save()
            messages.success(request, 'Your email login settings were updated!')
            return redirect('users:profile')
    else:
        # Create the email login settings form with the user's current settings
        form = EmailLoginSettingsForm(initial={
            'email_host': email_host,
            'email_port': email_port,
            'email_use_ssl': email_use_ssl
        })

    return render(request, 'users/profile.html', {'form': form})
