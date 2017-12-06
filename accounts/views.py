
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import messages, auth
from .forms import UserLoginForm, UserRegistrationForm
from medicalPractice.forms import DoctorRegistrationForm, PatientRegistrationForm
from medicalPractice.models import Doctor, Patient
from django.contrib.auth.decorators import login_required
# from blog.views import blogposts


# Create your views here.
def get_index(request):
    return render(request, 'index.html')
    
# Create your views here.
# def logout(request):
#     auth.logout(request)
#     messages.success(request, 'You have successfully logged out')
#     return redirect(blogposts)
    
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect("index")
    
    
def login(request):
    if request.method=="POST":
        form=UserLoginForm(request.POST)
        
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'])

            if user is not None:
                auth.login(request, user)
                messages.success(request, "You have successfully logged in")
                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(profile)
            else:
                form.add_error(None, "Your username or password was not recognised")
            
    else:
        form = UserLoginForm()
    
    return render(request, "login.html", {'form': form})

def registerDoctor(request):
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        typeForm = DoctorRegistrationForm(request.POST)
        
        if typeForm.is_valid():
            user = userForm.save()
            doctor = typeForm.save(commit=False)
            doctor.user = user
            doctor.save()
            
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password1'])
    
            if user is not None:
                auth.login(request, user)
                return redirect("index")
    else:
        form= UserRegistrationForm()
        typeForm = DoctorRegistrationForm()
    
    return render(request, "registerDoctor.html", {'form': form, 'typeForm': typeForm})
    
def registerPatient(request):
    if request.method=="POST":
        form = UserPatientRegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password1'])
                                     
            if user is not None:
                auth.login(request, user)
                return redirect("index")
    else:
        userForm= UserRegistrationForm()
        typeForm = PatientRegistrationForm()
    
    return render(request, "register.html", {'userForm': userForm, 'typeForm': typeForm})
    
@login_required()
def profile(request):
    return render(request, 'profile.html')