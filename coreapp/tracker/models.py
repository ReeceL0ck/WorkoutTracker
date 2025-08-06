from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Workout(models.Model):
    split_type   = models.CharField(max_length=200) # Upper/Lower, FullBody, Legs etc
    workout_date = models.DateTimeField("Date of workout")
    notes        = models.TextField(blank=True, help_text="Additional workout notes")
    def __str__(self):
        return f"{self.split_type()} - {self.workout_date.strftime('%Y-%m-%d')} - Notes : {self.notes}"
    
class Exercise(models.Model):
    '''
    Each Exercise is linked to a workout which is described above
    '''
    workout          = models.ForeignKey(
                        Workout, 
                        on_delete=models.CASCADE,
                        related_name='exercises'
                    )
    name_of_exercise = models.CharField(max_length=200)
    no_of_reps       = models.SmallIntegerField()
    no_of_sets       = models.SmallIntegerField()
    weight           = models.DecimalField(max_digits=5,decimal_places=2, help_text="Use KG")
    rpe_value        = models.PositiveIntegerField(
                        validators=[MinValueValidator(1), MaxValueValidator(10)],
                        null=True,
                        blank=True,
                        help_text="Rate of Perceived Exertion (1-10)"
                    )
    
    def __str__(self):
        return f"{self.name_of_exercise} : {self.no_of_sets}x{self.no_of_reps}"

