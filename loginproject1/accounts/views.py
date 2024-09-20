from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.http import HttpResponse

def home(request):
    return HttpResponse("welcome to home page ")

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home') #redirect to home after successful login
        else:
            messages.error(request,'Invalid username or password')
    return render(request,'accounts/login.html')