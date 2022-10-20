from urllib.robotparser import RequestRate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required

# Create your views here.


#login
def UserLogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request=request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("Dashboard:home")
                else:
                    return HttpResponse(
                        'You should Signup First or Account is disabled!')
            else:
                return HttpResponse('Invalid Login!')
    else:
        form = LoginForm()
    return render(request, 'Account/login.html', {'form': form})


#singup new user
def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if User.objects.filter(username=cd['username']).first():
                return render(
                    request, "Account/signup.html", {
                        'form': SignUpForm(),
                        "error": "Username has been Already Taken!"
                    })
            if cd['password1'] != cd['password2']:
                return render(
                    request, 'Account/signup.html', {
                        'form': SignUpForm(),
                        'error': "Password1 and Password2 should be match!"
                    })
            newuser = User.objects.create_user(username=cd['username'],
                                               password=cd['password1'])
            newuser.save()
            login(request, newuser)
            return HttpResponse("Signup Sucessfully Done!")
        else:
            return render(request, 'Account/signup.html', {
                'form': SignUpForm(),
                'error': "Invalid Data!"
            })
    else:
        return render(request, 'Account/signup.html', {'form': SignUpForm()})


@login_required
def UserLogout(request):
        logout(request)
        return redirect('Account:login')