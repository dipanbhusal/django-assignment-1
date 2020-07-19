from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import User, SignUp
# Create your views here.

UserModel = get_user_model()

def login_view(request):
    if request.method == 'POST':
        form = User(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'] ,
            password = form.cleaned_data['password'])
            if user:
                print('User can login')
                login(request, user)
                return redirect('blog-home')
            else:
                print('User is not registered in system. ')
            print(form.cleaned_data)
    elif request.method == 'GET':
        form = User()

    form = User()
    return render(request, 'users/login.html', {'form':form})



def logout_view(request):
    logout(request)
    return redirect( '/accounts/login/')

def signup_view(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            print(type(form.cleaned_data))
            user = UserModel(
                username = form.cleaned_data['username'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['email'],
            
            )
            user.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/accounts/login/')

    elif request.method == 'GET':
        form = SignUp()
        return render(request, 'users/signup.html', {'form':form})
    return render(request, 'users/signup.html', {'form':form})
