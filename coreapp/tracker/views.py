from django.shortcuts import render
from django.http import HttpResponse
from .forms import WorkoutForm

# Create your views here.
def index(request):
    return render(request, 'overview.html')

def workout(request):
    context ={}
    context['form']= WorkoutForm()

    return render(request, 'workout.html', context)
