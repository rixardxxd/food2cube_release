from django.http import HttpResponse

from django.shortcuts import render,get_object_or_404


def landing(request):

    return render(request,'mainSite/landing.html')# Create your views here.

def testing(request):

    return HttpResponse("You're looking at the results of poll.")
