from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExerciseForm, ViewProgress
from .models import Exercise
import json


def index(request):
    return render(request, 'index.html')

def graphing(request):
    exercise_name = 'rdl' 
    try:
        exercise = Exercise.objects.filter(name_of_exercise=exercise_name).first()
        page_title = f"{exercise.get_name_of_exercise_display()} Progress"
    except Exercise.DoesNotExist:
        page_title = "No Data Found"
    datapoints = [
        {"label": ex.name_of_exercise,
         "x": ex.workout_date.strftime("%Y-%m-%d"),
         "y": float(ex.weight),
         "z": ex.no_of_reps} for ex in Exercise.objects.filter(name_of_exercise=f'{exercise_name}').order_by('workout_date')
    ]
    

    datapoints = json.dumps(datapoints)

    return render(request, 'graphing.html', context={'graph_data':datapoints, 'page_title':page_title})                        

def overview(request):
    context = {}
    context['form']= ViewProgress() 
    if request.method == "POST":
        form = ViewProgress(request.POST)
        if form.is_valid():
            name_option = form.cleaned_data['name_option']
            exercise_from_db = Exercise.objects.filter(name_of_exercise=name_option).order_by('workout_date')
            # print(exercise_from_db.values()[0]) # How to get indivual value from <DataSet>
            try:    
                for i in range(len(exercise_from_db.values())):
                    print(exercise_from_db.values()[i])
            except IndexError:
                print('None found!')
            context['Exercises'] = exercise_from_db
        else:
            context['form'] = ViewProgress()
    else:   
        context['form'] = ViewProgress()
    
    return render(request, 'overview.html', context)

def workout(request):
    context ={}
    context['form']= ExerciseForm() 

    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():

            date = form.cleaned_data['date']
            name_of_exercise = form.cleaned_data['name_of_exercise']
            no_of_reps = form.cleaned_data['no_of_reps']
            no_of_sets = form.cleaned_data['no_of_sets']
            weight = form.cleaned_data['weight']
            rpe_value = form.cleaned_data['rpe_value']
            notes = form.cleaned_data['notes']
            
            new_exercise = Exercise(
                workout_date=date,
                name_of_exercise=name_of_exercise,
                no_of_reps=no_of_reps,
                no_of_sets=no_of_sets,
                weight=weight,
                rpe_value=rpe_value,
                notes=notes
            )
            new_exercise.save()

            form = ExerciseForm() 

        else:
            form = ExerciseForm()

    return render(request, 'workout.html', context)
