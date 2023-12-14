from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
def HomePage(request):
   
    return render(request,'home.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        my_user = User.objects.create_user(uname, email, password)
        my_user.save()
        print(uname, email, password)
        return redirect('login')
        
    return render(request, 'signup.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passw = request.POST.get('password')
        print(username, passw)
        user=authenticate(request,username=username,password=passw)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrect")
    return render(request,'login.html')

