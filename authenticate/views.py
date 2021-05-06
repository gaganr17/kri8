#used to redirect the new users to their respective domain
from django.shortcuts import render,redirect
#used to obtain the inbuilt form for signup and signin
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
#used to create an User
from django.contrib.auth.models import User
#used to uniquely identify new users
from django.db import IntegrityError
#used to redirect to the user's domain and also kick em outa it
from django.contrib.auth import login,logout,authenticate

def signupuser(request):
    if request.method == 'GET':
        return render(request,'authenticate/signupuser.html',{'form':UserCreationForm()})

    else:
        if(request.POST['password1']==request.POST['password2']):

            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('index')
            except IntegrityError:
                return render(request,'authenticate/signupuser.html',{'form':UserCreationForm(),'error': 'That username has already been taken. Please choose a new username'})
        else:
            return render(request,'authenticate/signupuser.html',{'form':UserCreationForm(),'error': 'The Passwords did not match!'})

def signinuser(request):
    if request.method == 'GET':
        return render(request,'authenticate/signinuser.html',{'form':AuthenticationForm()})

    else:
        user = authenticate(request,username=request.POST['username'],password = request.POST['password'])
        if user is None:
            return render(request,'authenticate/signinuser.html',{'form':AuthenticationForm(),'error':'Invalid Username or Password. Please try again.'})
        else:
            login(request,user)
            return redirect('index')


def logoutuser(request):
    if(request.method == 'POST'):
        logout(request)
        return redirect('index')


# def authn(request):
#     return render(request,'authenticate/index.html')

# def test1(request):
#     return render(request,'authenticate/test1.html')

def index(request):
    return render(request, "index/index.html")
