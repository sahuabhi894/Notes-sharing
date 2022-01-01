from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages 
from datetime import date

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
        error=""
        try:

            if user.is_superuser:
                login(request,user)
                messages.success(request, "Successfully Logged In")
                return redirect("admin_home")
                error="no"

            elif user is not None:
                login(request,user)
                messages.success(request, "Successfully Logged In")
                return redirect("profile")
                error="no"
        
        except:
                error="yes"
                messages.error(request, "Invalid credentials! Please try again")
                return redirect("index")
    
    return HttpResponse("404- Not found")
   

    return HttpResponse("login")
                
           
    




def admin_home(request):
    if not request.user.is_staff:
        return redirect('index')
    pn= Notes.objects.filter(status="pending").count()
    an= Notes.objects.filter(status="Accept").count()
    rn= Notes.objects.filter(status="Reject").count()
    alln= Notes.objects.all().count()
    d={'pn':pn,'an':an,'rn':rn,'alln':alln}
    return render(request,'notes/admin_home.html',d)

def profile(request):
    if not request.user.is_authenticated:
        return redirect('index')
    user = User.objects.get(id= request.user.id)
    data = Signup.objects.get(user=user)
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



def changepassword(request):
    if not request.user.is_authenticated:
        return redirect('index')
    
    if request.method=="POST":
        o=request.POST['old']
        n=request.POST['new']
        c=request.POST['confirm']
        if c==n:
            u=User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            
            return redirect('index')
        else:
            messages.error(request, " Passwords do not match")
            return redirect('profile')

           
     
    return render(request,'notes/changepassword.html')




def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('index')
    user = User.objects.get(id= request.user.id)
    data = Signup.objects.get(user=user)
    if request.method =='POST':
        f= request.POST['firstname']
        l= request.POST['lastname']
        b= request.POST['branch']
        user.first_name=f
        user.last_name=l
        data.branch=b
        user.save()
        data.save()
        return redirect('profile')
        
    d={'data':data,'user':user}

    return render(request,'notes/edit_profile.html',d)

def upload_notes(request):
    if not request.user.is_authenticated:
            return redirect('index')
    if request.method=="POST":
        # Get the post parameters
        b=request.POST['branch']
        s=request.POST['subject']
        n=request.FILES['notesfile']
        d=request.POST['description']
        y=request.POST['year']
        nt=request.POST['notestype']
        u =User.objects.filter(username=request.user.username).first()

        Notes.objects.create(user=u,uploadingdate=date.today(),branch=b,subject=s,notesfile=n,description=d,year=y,notestype=nt,status='pending')    
        
    return render(request,'notes/upload_notes.html')


def view_mynotes(request):
    if not request.user.is_authenticated:
           return redirect('index')
    user = User.objects.get(id= request.user.id)
    notes = Notes.objects.filter(user=user)
    d={'notes':notes}
    return render(request,'notes/view_mynotes.html',d)



def delete_mynotes(request,pid):
    if not request.user.is_authenticated:
           return redirect('index')
    notes=Notes.objects.get(id=pid)
    notes.delete()
    return redirect('view_mynotes')



def view_users(request):
    if not request.user.is_authenticated:
           return redirect('index')
    users = Signup.objects.all()
    d={'users':users}
    return render(request,'notes/view_users.html',d)
    


def delete_users(request,pid):
    if not request.user.is_authenticated:
           return redirect('index')
    user=User.objects.get(id=pid)
    user.delete()
    return redirect('view_users')


def pending_notes(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(status= "pending")
    d={'notes':notes}
    return render(request,'notes/pending_notes.html',d)

def accepted_notes(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(status= "Accept")
    d={'notes':notes}
    return render(request,'notes/accepted_notes.html',d)

def rejected_notes(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(status= "Reject")
    d={'notes':notes}
    return render(request,'notes/rejected_notes.html',d)

def all_notes(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.all()
    d={'notes':notes}
    return render(request,'notes/all_notes.html',d)



def assign_status(request,pid):
    if not request.user.is_authenticated:
           return redirect('index')
    notes=Notes.objects.get(id=pid)

    if request.method=='POST':
        s=request.POST['status']
        notes.status=s
        notes.save()
        return redirect('admin_home')
    d={'notes':notes}
    return render(request,'notes/assign_status.html',d)


def delete_notes(request,pid):
    if not request.user.is_authenticated:
           return redirect('index')
    notes=Notes.objects.get(id=pid)
    notes.delete()
    return redirect('all_notes')

def viewallnotes(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.all()
    d={'notes':notes}
    return render(request,'notes/viewallnotes.html',d)


def first_year(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "1st Year")
    d={'notes':notes}
    return render(request,'notes/first_year.html',d)

def second_year(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "2nd Year")
    d={'notes':notes}
    return render(request,'notes/second_year.html',d)

def third_year(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "3rd Year")
    d={'notes':notes}
    return render(request,'notes/third_year.html',d)

def forth_year(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "4th Year")
    d={'notes':notes}
    return render(request,'notes/forth_year.html',d)

def other(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "Other" , notestype="Others")
    d={'notes':notes}
    return render(request,'notes/other.html',d)

def cse1(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "1st Year" , branch= "Computer Science")
    d={'notes':notes}
    return render(request,'notes/cse1.html',d)

def ece1(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "1st Year" , branch = "Electronics And Communication")
    d={'notes':notes}
    return render(request,'notes/ece1.html',d)

def cse2(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "2nd Year" , branch= "Computer Science")
    d={'notes':notes}
    return render(request,'notes/cse2.html',d)

def ece2(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "2nd Year" , branch = "Electronics And Communication")
    d={'notes':notes}
    return render(request,'notes/ece2.html',d)

def cse3(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "3rd Year" , branch= "Computer Science")
    d={'notes':notes}
    return render(request,'notes/cse3.html',d)

def ece3(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "3rd Year" , branch = "Electronics And Communication")
    d={'notes':notes}
    return render(request,'notes/ece3.html',d)

def cse4(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "4th Year" , branch= "Computer Science")
    d={'notes':notes}
    return render(request,'notes/cse4.html',d)

def ece4(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "4th Year" , branch = "Electronics And Communication")
    d={'notes':notes}
    return render(request,'notes/ece4.html',d)

def assignment_cse_1(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "1st Year" , branch = "Computer Science" , notestype="Assignment")
    d={'notes':notes}
    return render(request,'FirstYear/assignment_cse_1.html',d)

def assignment_ece_1(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "1st Year" , branch = "Electronics And Communication" ,notestype="Assignment")
    d={'notes':notes}
    return render(request,'FirstYear/assignment_ece_1.html',d)

def book_cse_1(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "1st Year" , branch = "Computer Science" , notestype="Book")
    d={'notes':notes}
    return render(request,'FirstYear/book_cse_1.html',d)

def book_ece_1(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "1st Year" , branch = "Electronics And Communication" ,notestype="Book")
    d={'notes':notes}
    return render(request,'FirstYear/book_ece_1.html',d)

def cl_cse_1(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "1st Year" , branch = "Computer Science" , notestype="Class Notes")
    d={'notes':notes}
    return render(request,'FirstYear/cl_cse_1.html',d)

def cl_ece_1(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "1st Year" , branch = "Electronics And Communication" ,notestype="Class Notes")
    d={'notes':notes}
    return render(request,'FirstYear/cl_ece_1.html',d)

def others_cse_1(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "1st Year" , branch = "Computer Science" , notestype="Others")
    d={'notes':notes}
    return render(request,'FirstYear/others_cse_1.html',d)

def others_ece_1(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "1st Year" , branch = "Electronics And Communication" ,notestype="Others")
    d={'notes':notes}
    return render(request,'FirstYear/others_ece_1.html',d)

def qp_cse_1(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "1st Year" , branch = "Computer Science" , notestype="Question Paper")
    d={'notes':notes}
    return render(request,'FirstYear/qp_cse_1.html',d)

def qp_ece_1(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "1st Year" , branch = "Electronics And Communication" ,notestype="Question Paper")
    d={'notes':notes}
    return render(request,'FirstYear/qp_ece_1.html',d)

# ...................................................................................................................
def assignment_cse_2(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "2nd Year" , branch = "Computer Science" , notestype="Assignment")
    d={'notes':notes}
    return render(request,'SecondYear/assignment_cse_2.html',d)

def assignment_ece_2(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "2nd Year" , branch = "Electronics And Communication" ,notestype="Assignment")
    d={'notes':notes}
    return render(request,'SecondYear/assignment_ece_2.html',d)

def book_cse_2(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "2nd Year" , branch = "Computer Science" , notestype="Book")
    d={'notes':notes}
    return render(request,'SecondYear/book_cse_2.html',d)

def book_ece_2(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "2nd Year" , branch = "Electronics And Communication" ,notestype="Book")
    d={'notes':notes}
    return render(request,'SecondYear/book_ece_2.html',d)

def cl_cse_2(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "2nd Year" , branch = "Computer Science" , notestype="Class Notes")
    d={'notes':notes}
    return render(request,'SecondYear/cl_cse_2.html',d)

def cl_ece_2(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "2nd Year" , branch = "Electronics And Communication" ,notestype="Class Notes")
    d={'notes':notes}
    return render(request,'SecondYear/cl_ece_2.html',d)

def others_cse_2(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "2nd Year" , branch = "Computer Science" , notestype="Others")
    d={'notes':notes}
    return render(request,'SecondYear/others_cse_2.html',d)

def others_ece_2(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "2nd Year" , branch = "Electronics And Communication" ,notestype="Others")
    d={'notes':notes}
    return render(request,'SecondYear/others_ece_2.html',d)

def qp_cse_2(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "2nd Year" , branch = "Computer Science" , notestype="Question Paper")
    d={'notes':notes}
    return render(request,'SecondYear/qp_cse_2.html',d)

def qp_ece_2(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "2nd Year" , branch = "Electronics And Communication" ,notestype="Question Paper")
    d={'notes':notes}
    return render(request,'SecondYear/qp_ece_2.html',d)

# ...............................................................................................................................

def assignment_cse_3(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "3rd Year" , branch = "Computer Science" , notestype="Assignment")
    d={'notes':notes}
    return render(request,'ThirdYear/assignment_cse_3.html',d)

def assignment_ece_3(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "3rd Year" , branch = "Electronics And Communication" ,notestype="Assignment")
    d={'notes':notes}
    return render(request,'ThirdYear/assignment_ece_3.html',d)

def book_cse_3(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "3rd Year" , branch = "Computer Science" , notestype="Book")
    d={'notes':notes}
    return render(request,'ThirdYear/book_cse_3.html',d)

def book_ece_3(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "3rd Year" , branch = "Electronics And Communication" ,notestype="Book")
    d={'notes':notes}
    return render(request,'ThirdYear/book_ece_3.html',d)

def cl_cse_3(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "3rd Year" , branch = "Computer Science" , notestype="Class Notes")
    d={'notes':notes}
    return render(request,'ThirdYear/cl_cse_3.html',d)

def cl_ece_3(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "3rd Year" , branch = "Electronics And Communication" ,notestype="Class Notes")
    d={'notes':notes}
    return render(request,'ThirdYear/cl_ece_3.html',d)

def others_cse_3(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "3rd Year" , branch = "Computer Science" , notestype="Others")
    d={'notes':notes}
    return render(request,'ThirdYear/others_cse_3.html',d)

def others_ece_3(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "3rd Year" , branch = "Electronics And Communication" ,notestype="Others")
    d={'notes':notes}
    return render(request,'ThirdYear/others_ece_3.html',d)

def qp_cse_3(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "3rd Year" , branch = "Computer Science" , notestype="Question Paper")
    d={'notes':notes}
    return render(request,'ThirdYear/qp_cse_3.html',d)

def qp_ece_3(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "3rd Year" , branch = "Electronics And Communication" ,notestype="Question Paper")
    d={'notes':notes}
    return render(request,'ThirdYear/qp_ece_3.html',d)

# ................................................................................................................................
def assignment_cse_4(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "4th Year" , branch = "Computer Science" , notestype="Assignment")
    d={'notes':notes}
    return render(request,'FourthYear/assignment_cse_4.html',d)

def assignment_ece_4(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "4th Year" , branch = "Electronics And Communication" ,notestype="Assignment")
    d={'notes':notes}
    return render(request,'FourthYear/assignment_ece_4.html',d)

def book_cse_4(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "4th Year" , branch = "Computer Science" , notestype="Book")
    d={'notes':notes}
    return render(request,'FourthYear/book_cse_4.html',d)

def book_ece_4(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "4th Year" , branch = "Electronics And Communication" ,notestype="Book")
    d={'notes':notes}
    return render(request,'FourthYear/book_ece_4.html',d)

def cl_cse_4(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "4th Year" , branch = "Computer Science" , notestype="Class Notes")
    d={'notes':notes}
    return render(request,'FourthYear/cl_cse_4.html',d)

def cl_ece_4(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "4th Year" , branch = "Electronics And Communication" ,notestype="Class Notes")
    d={'notes':notes}
    return render(request,'FourthYear/cl_ece_4.html',d)

def others_cse_4(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "4th Year" , branch = "Computer Science" , notestype="Others")
    d={'notes':notes}
    return render(request,'FourthYear/others_cse_4.html',d)

def others_ece_4(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "4th Year" , branch = "Electronics And Communication" ,notestype="Others")
    d={'notes':notes}
    return render(request,'FourthYear/others_ece_4.html',d)

def qp_cse_4(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "4th Year" , branch = "Computer Science" , notestype="Question Paper")
    d={'notes':notes}
    return render(request,'FourthYear/qp_cse_4.html',d)

def qp_ece_4(request):
    if not request.user.is_authenticated:
           return redirect('index')
    notes = Notes.objects.filter(year= "4th Year" , branch = "Electronics And Communication" ,notestype="Question Paper")
    d={'notes':notes}
    return render(request,'FourthYear/qp_ece_4.html',d)