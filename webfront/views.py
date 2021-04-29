from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Patient,Instructor

#home page
def index(request):

    context = {}

    if request.user.is_authenticated:
        patients = Patient.objects.filter(user=request.user)
        instructors = Instructor.objects.filter(user=request.user)

        context = {'patients':patients, 'instructors' : instructors

        }


    return render(request, 'webfront/index.html', context)


def about(request):

    return render(request, 'webfront/about.html')
