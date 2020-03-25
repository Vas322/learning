from django.urls import path
from . import views

urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Вывод всех пицц.
    path('pizzas/', views.pizzas, name='pizzas'),
    # Страница с подробной информацией по отдельной теме
    path(r'pizzas/<pizza_id>/', views.pizza, name='pizza'),
]
