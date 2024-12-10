from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=255)
    carbs = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()
    calories = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name
    

class Consume(models.Model):
    consumed_food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="consumes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="consumes")
    