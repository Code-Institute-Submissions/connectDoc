
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import messages, auth
from .forms import UserLoginForm, UserRegistrationForm
from medicalPractice.forms import DoctorRegistrationForm, PatientRegistrationForm, ClinicRegistrationForm
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
        user_form = UserRegistrationForm(request.POST, request.FILES    )
        usertype_form = DoctorRegistrationForm(request.POST, request.FILES)

        if user_form.is_valid() and usertype_form.is_valid():
            user = user_form.save()
            doctor = usertype_form.save(commit=False)
            doctor.user = user
            doctor.save()

            user = auth.authenticate(username=user_form.cleaned_data['username'],
                                     password=user_form.cleaned_data['password1'])

            if user is not None:
                auth.login(request, user)
                return redirect("index")
    else:
        user_form= UserRegistrationForm()
        usertype_form = DoctorRegistrationForm()

    return render(request, "register.html", {'form': user_form, 'typeForm': usertype_form})

def registerPatient(request):
    if request.method=="POST":
        user_form = UserRegistrationForm(request.POST)
        usertype_form = PatientRegistrationForm(request.POST)

        if user_form.is_valid() and usertype_form.is_valid():
            user = user_form.save()
            patient = usertype_form.save(commit=False)
            patient.user = user
            patient.save()

            user = auth.authenticate(username=user_form.cleaned_data['username'],
                                     password=user_form.cleaned_data['password1'])

            if user is not None:
                auth.login(request, user)
                return redirect("index")
    else:
        user_form= UserRegistrationForm()
        usertype_form = PatientRegistrationForm()

    return render(request, "register.html", {'form': user_form, 'typeForm': usertype_form})


def registerClinic(request):
    if request.method=="POST":
        user_form = UserRegistrationForm(request.POST, request.FILES    )
        usertype_form = ClinicRegistrationForm(request.POST, request.FILES)

        if user_form.is_valid() and usertype_form.is_valid():
            user = user_form.save()
            clinic = usertype_form.save(commit=False)
            clinic.user = user
            clinic.save()

            user = auth.authenticate(username=user_form.cleaned_data['username'],
                                     password=user_form.cleaned_data['password1'])

            if user is not None:
                auth.login(request, user)
                return redirect("index")
    else:
        user_form= UserRegistrationForm()
        usertype_form = ClinicRegistrationForm()

    return render(request, "register.html", {'form': user_form, 'typeForm': usertype_form})


@login_required()
def profile(request):
    return render(request, 'profile.html')