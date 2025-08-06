from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello This is where you can track")

def workout(request):
    return HttpResponse("This is where you can make add a workout")
