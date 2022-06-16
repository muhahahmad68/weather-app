from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django import forms  # customizing our form
from django.contrib.auth.models import User  # django default user model
from django.contrib import messages
# Create your views here.


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('weather')
        else:
            messages.info(request, "username or password is incorrect")

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')  # get username
            messages.success(request, 'Account successfully created for ' + user)  # print success message

            return redirect('login')  # redirect to login page after successful sign up
    return render(request, 'register.html', {'form': form})
