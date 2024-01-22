from django.shortcuts import render,redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages


# Create your views here.
def loginn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username , password=password)
        
        if user is not None:
            auth.login(request,user)
            name= user.first_name
            return redirect('home/',{'first': name })

        else:
            messages.info(request,"Doesnt Match")
            return redirect('/')
    else:
        return render(request, 'login.html') 
    
def logout(request):
    auth.logout(request)
    return render(request,'/')

def registerr(request):
    return render(request,'register.html')

def register(request):
    if request.method == "POST":
        first_name= request.POST['name']
        username = request.POST['username']
        password = request.POST['password'] 
        user= User.objects.create_user(first_name= first_name,username=username,password=password)
        user.save();
        return render(request, "login.html",{"user":first_name})
        
    else:
        return render(request  ,'register.html') 
