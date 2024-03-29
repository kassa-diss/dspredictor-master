from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages,auth
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from datetime import datetime
from .forms import *
from django.db import models
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    View,
    CreateView,
    UpdateView,
    ListView,
    DeleteView,
    TemplateView,
)

from .models import Patient,Instructor
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar

from .models import *
from .utils import Calendar
from .forms import EventForm


 #login function
@unauthenticated_user
def login(request):
     if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username=username, password=password)

       if user is not None:
         auth.login(request, user)
         messages.success(request, 'Welcome')
         return redirect('index')
       else:
         messages.error(request, 'Invalid credentials')
         return redirect('login')
     else:
       return render(request, 'accounts/login.html')


#Signup function
@unauthenticated_user
def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being used')
          return redirect('register')
        else:
          # Looks good
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
          group = Group.objects.get(name='patients')
          user.groups.add(group)
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('edit-profile')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register')
  else:
    return render(request, 'accounts/register.html')



#logout
def logout(request):
    if request.method == 'POST':
      auth.logout(request)
      messages.success(request, 'You are now logged out')
      return redirect('login')


def PatientCreateView (request):
    if request.method == 'GET':
            return render(request,'accounts/edit_profile.html',{'form':PatientForm()})
    else:
        form = PatientForm(request.POST,request.FILES or None)
        if form.is_valid():
            print("valid")
            new_UserProfileForm = form.save(commit=False)
            new_UserProfileForm.user = request.user
            new_UserProfileForm.save()

        return render(request,'accounts/edit_profile.html',{'form':PatientForm()})


# used to update a profile info
class PatientUpdateView(SuccessMessageMixin, UpdateView):
    model = Patient
    form_class = PatientForm
    success_url = 'edit-profile'
    success_message = "Yor details has been updated successfully"
    template_name = "accounts/edit_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["savebtn"] = 'Save Changes'

        return context


class PatientProfileView(View):
    def get(self, request, pk):
        UserProfileObj = get_object_or_404(Patient, pk=pk)

        context = {
            'UserProfile'  : UserProfileObj,
        }
        return render(request, 'accounts/patient_profile.html', context)

class InstructorProfileView(View):
    def get(self, request, pk):
        UserProfileObj = get_object_or_404(Instructor, pk=pk)

        context = {
            'UserProfile'  : UserProfileObj,
        }
        return render(request, 'accounts/instructor_profile.html', context)


def Patients(request):
  UserProfileObj = Patient.objects.order_by('p_id')

  paginator = Paginator(UserProfileObj, 8)
  page = request.GET.get('page')
  paged_patients = paginator.get_page(page)

  context = {
    'Patients': paged_patients
  }

  return render(request, 'accounts/patients.html', context)



def Instructors(request):
    UserProfileObj = Instructor.objects.order_by('in_id')

    paginator = Paginator(UserProfileObj, 8)
    page = request.GET.get('page')
    paged_instructors = paginator.get_page(page)

    context = {
      'Instructors': paged_instructors
    }

    return render(request, 'accounts/instructors.html', context)

class InstructorUpdateView(SuccessMessageMixin, UpdateView):
    model = Instructor
    form_class = InstructorForm
    success_url = 'instructor'
    success_message = "Yor details has been updated successfully"
    template_name = "accounts/insedit_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["savebtn"] = 'Save Changes'

        return context


def PatientMyProfile(request):
    pro = Patient.objects.filter(user=request.user)
    my = MyWorks.objects.filter(user=request.user)
    return render(request,'accounts/PatientMyProfile.html',{'pro':pro,'my':my})


def InstructorMyProfile(request):
    pro = Instructor.objects.filter(user=request.user)
    return render(request,'accounts/InstructorMyProfile.html',{'pro':pro})


def MyWorksCreateView (request):
    if request.method == 'GET':
            return render(request,'accounts/add_my_works.html',{'form':MyWorksForm()})
    else:
        form = MyWorksForm(request.POST,request.FILES or None)
        if form.is_valid():
            print("valid")

            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()

        return redirect('myprofile-patient')


def talent(request):
    my = MyWorks.objects.all()
    return render(request,'accounts/my.html',{'my':my})




class CalendarView(generic.ListView):
    model = Event
    template_name = 'accounts/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.user = request.user
        form.save()

        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'accounts/event.html', {'form': form})
