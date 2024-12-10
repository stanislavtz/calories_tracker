from django.shortcuts import render
from .models import Food, Consume

# Create your views here.
def index(request):
    foods = Food.objects.all()

    if request.method == "POST":
        selected_food = request.POST.get("foods")

        food = Food.objects.get(name=selected_food)
        user = request.user

        consume = Consume(consumed_food=food, user=user)
        consume.save()

    user_consumed_food = request.user.consumes.all()

    for i in range(len(user_consumed_food)):
        user_consumed_food[i].curr_number = i+1

    total_carbs = sum(f.consumed_food.carbs for f in user_consumed_food)
    total_proteins = sum(f.consumed_food.proteins for f in user_consumed_food)
    total_fats = sum(f.consumed_food.fats for f in user_consumed_food)
    total_calories = sum(f.consumed_food.calories for f in user_consumed_food)

    context = {
        "foods": foods,
        "consumes": user_consumed_food,
        "total_carbs": total_carbs,
        "total_proteins": total_proteins,
        "total_fats": total_fats,
        "total_calories": total_calories
    }

    return render(request, "myapp/index.html", context)