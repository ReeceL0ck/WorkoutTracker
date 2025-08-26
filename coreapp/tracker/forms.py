from django import forms
from .models import EXERCISE_CHOICES

class ExerciseForm(forms.Form):
    def __init__(self, *args, **kwargs): # Initialize the form with custom attributes for custom css for each field
        super(ExerciseForm, self).__init__(*args, **kwargs)
        self.fields['notes'].widget.attrs['style'] = "height:100px"

    date             = forms.DateField(label='Date', widget=forms.DateInput(attrs={'type': 'date'}))
    name_of_exercise = forms.ChoiceField(choices=EXERCISE_CHOICES, label='Exercise Name')
    no_of_reps       = forms.IntegerField(label='Number of Reps', min_value=1,max_value=20)
    no_of_sets       = forms.IntegerField(label='Number of Sets', min_value=1,max_value=20)
    weight           = forms.DecimalField(label='Weight (kg)', max_digits=5, decimal_places=2, min_value=0.0, max_value=500, required=False)
    rpe_value        = forms.IntegerField(
                label='RPE Value',
                min_value=1,
                max_value=10,
                required=False
    )
    notes            = forms.CharField(label='Notes', widget=forms.Textarea, required=False)



class ViewProgress(forms.Form):
    EXERCISE_CHOICES.insert(0, ('', 'Select Exercise'))  # Add an empty choice for the dropdown
    name_option      = forms.ChoiceField(choices=EXERCISE_CHOICES,
                                         label='',
                                         widget=forms.Select(attrs={'onchange': 'submit();'}))  