from django.db import models


# Create your models here.
class Pizza(models.Model):
    """Выводит виды пиццы"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.name


class Topping(models.Model):
    """Информация о добавках"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    addition = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Атрибут, позволяющий использовать форму множественного числа 'Toppings' """
        verbose_name_plural = 'toppings'

    def __str__(self):
        """Возвращает строковое представление модели."""
        if len(self.addition) <= 50:
            return self.addition
        return self.addition[:50] + "..."
