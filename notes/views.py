from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages 

# Create your views here.
def about(request):
    return render(request , 'notes/about.html')


# Create your views here.
def index(request):
    return render(request , 'notes/index.html')


def handleLogin(request):
    if request.method == 'POST':
        u=request.POST['loginadminname']
        p=request.POST['loginadminpassword']
        user = authenticate(username=u, password=p)

        if user.is_superuser:
            login(request,user)
            messages.success(request, "Successfully Logged In")
            return redirect("admin_home")

        elif user is not None:
            login(request,user)
            messages.success(request, "Successfully Logged In")
            return redirect("profile")

        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("index")

    return HttpResponse("404- Not found")
   

    return HttpResponse("login")
                
           
    




def admin_home(request):
    if not request.user.is_staff:
        return redirect('index')
    return render(request,'notes/admin_home.html')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('index')
    user = User.objects.get(id= request.user.id)
    data = Signup.objects.filter(user=user)
    d={'data':data,'user':user}

    return render(request,'notes/profile.html',d)


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('index')

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        branch=request.POST['branch']
        role=request.POST['role']

        # check for errorneous input
        
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('index')
        
        # Create the user
        user = User.objects.create_user(username=username, email=email, password=pass1,first_name= fname,last_name= lname)
        Signup.objects.create(user=user,branch=branch,role=role)
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('index')

    else:
        return HttpResponse("404 - Not found")
