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

    context = {
        "foods": foods
    }

    return render(request, "myapp/index.html", context)