from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required



from .models import Departments,Doctors
from .forms import BookingForm



# Create your views here.


def loginn(request):
     if request.user.is_authenticated:
        return redirect(index)
    
     if request.method == "POST":
      username = request.POST['username']
      password = request.POST['password']

         # authenticate the user check the user is available
      user = authenticate(username=username,password=password)

      if user is not None:
        
         # login the user
         login(request,user)
         return render(request, 'dj index.html')
      
      else:
        
          return redirect('login')
   
      
     return render(request, 'login.html',)

def signup(request):
   if request.method == "POST":
      print(request.method)
      print(request.POST)
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']

      if User.objects.filter(username=username).exists():
         return redirect('signup')
      myuser=User.objects.create_user(username,email,password) # used to create a user
      myuser.save() # save the user into database

     

        # Redirect to the login page
      return redirect('login')

   return render(request, 'signup.html')





   





def index(request):
   if request.user.is_authenticated:
     return render(request, 'dj index.html')
   return redirect(loginn)
    
def about(request):
   if request.user.is_authenticated:
    return render(request,'about.html')
   return redirect(loginn)


def booking(request):
   if request.user.is_authenticated:
    
     if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save() 
            return render(request,'succes.html')
    

     form = BookingForm()
     dict_form={
       'form' : form
    }
     return render(request,'booking.html', dict_form)
   return redirect(loginn)
   
      

def docters(request):
   # check the user is authenticated
   if request.user.is_authenticated:
    dict_docs={
       "doctors": Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs )

   return redirect(loginn)
def condact(request):
 if request.user.is_authenticated:
   return render(request,'contact.html')
 return redirect(loginn)

def department(request):
   if request.user.is_authenticated:
   
    dict_dept={
       "dept": Departments.objects.all()
    }
    return render(request, 'department.html',dict_dept)
   return redirect(loginn)

def logout(request):
   if request.user.is_authenticated:
      request.session.flush()
   return redirect(loginn)





   
   

  