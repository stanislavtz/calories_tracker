from django.contrib import admin
from .models import Food

# Register your models here.
class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "id", "carbs", "proteins", "fats", "calories")
    list_filter = ("carbs", "proteins", "fats", "calories")


admin.site.register(Food, FoodAdmin)
