from django.shortcuts import render
from main.models import Dish




def home(request):
    dishes = Dish.objects.all()
    return render(request, 'restaurant/home.html', {'dishes': dishes})
