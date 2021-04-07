from django.shortcuts import render
from django.http import HttpResponse

#home page
def index(request):


    context = {

    }

    return render(request, 'webfront/index.html', context)
