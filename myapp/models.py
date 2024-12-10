from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=255)
    carbs = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()
    calories = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name