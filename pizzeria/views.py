from django.shortcuts import render
from .models import Pizza


# Создайте здесь свои представления.
def index(request):
    """Домашняя страница приложения pizzeria"""
    return render(request, 'pizzeria/index.html')


def pizzas(request):
    """Выводит список пицц."""
    pizzas = Pizza.objects.order_by('date_added')  # Параметр сортировки. В данном случае по дате сортирует
    context = {'pizzas': pizzas}
    return render(request, 'pizzeria/pizzas.html', context)


def pizza(request, pizza_id):
    """Выводит добавки к пицце."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-date_added')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzeria/pizza.html', context)
