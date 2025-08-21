from django import forms


class WorkoutForm(forms.Form):
    split_type = forms.CharField(label='Split Type', max_length=100)
    date = forms.DateField(label='Date', widget=forms.SelectDateWidget())
    notes = forms.CharField(label='Additional Notes',max_length=250)


class ExerciseForm(forms.Form):
    name_of_exercise = forms.CharField(label='Name of Exercise', max_length=100)
    no_of_reps = forms.IntegerField(label='Number of Reps', min_value=1)
    no_of_sets = forms.IntegerField(label='Number of Sets', min_value=1)
    weight = forms.DecimalField(label='Weight (kg)', max_digits=5, decimal_places=2, min_value=0.0, required=False)
    rpe_value = forms.IntegerField(
        label='RPE Value',
        min_value=1,
        max_value=10,
        required=False,
        help_text="Rate of Perceived Exertion (1-10)"
    )
