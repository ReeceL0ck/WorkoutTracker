from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

EXERCISE_CHOICES = [
    ('squat', 'Squat'),
    ('deadlift', 'Deadlift'),
    ('rdl', 'Romanian Deadlift (RDL)'),
    ('benchpress', 'Bench Press'),
    ('inclinebenchpress', 'Incline Bench Press'),
    ('dumbellpress', 'Dumbell Press'),
    ('inclinedumbellpress', 'Incline Dumbell Press'),
    ('pullup', 'Pull Up'),
    ('overheadpress', 'Overhead Press'),
    ('lunge', 'Lunge'),
    ('bicepcurl', 'Bicep Curl'),
    ('tricepdip', 'Tricep Dip'),
    ('triceppushdown', 'Tricep Pushdown'),
    ('skullcrusher', 'Skull Crusher'),
    ('legpress', 'Leg Press'),
    ('lateralraise', 'Lateral Raise'),
    ('latpulldown', 'Lat Pulldown'),
    ('legcurl', 'Leg Curl'),
    ('calfraise', 'Calf Raise'),
    ('legextension', 'Leg Extension'),
    ('stepup', 'Step Ups'),
    ('hipabduction', 'Hip Abduction'),
    ('kickbacks', 'Kickbacks'),
    ('seatedrow', 'Seated Row'),
    ('hipthrust', 'Hip Thrust'),
    ('pecfly', 'Pec Fly'),
    ('dumbellshoulderpress', 'Dumbell Shoulder Press'),
    ('facepull', 'Face Pull'),

]

    
class Exercise(models.Model):
    workout_date     = models.DateTimeField("Date of workout", default=None)
    notes            = models.TextField(blank=True, help_text="Additional workout notes")
    name_of_exercise = models.CharField(max_length=200,choices=EXERCISE_CHOICES)
    no_of_reps       = models.SmallIntegerField()
    no_of_sets       = models.SmallIntegerField()
    weight           = models.DecimalField(max_digits=5,decimal_places=2, help_text="Use KG")
    rpe_value        = models.PositiveIntegerField(
                        validators=[MinValueValidator(1), MaxValueValidator(10)],
                        null=True,
                        blank=True,
                        help_text="Rate of Perceived Exertion (1-10)"
                    )
    user             = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return f"{self.get_name_of_exercise_display()} : {self.no_of_sets}x{self.no_of_reps}"


