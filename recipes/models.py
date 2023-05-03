from django.db import models
from django.contrib.auth import get_user_model
from collections import defaultdict

User = get_user_model()

class Cuisine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кухня'
        verbose_name_plural = 'Кухня'

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='dishes/')
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient, through='DishIngredient')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюдо'

class DishIngredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ингредиенты для блюдо'
        verbose_name_plural = 'Ингредиенты для блюдо'


class Generator(models.Model):
  generator = models.ManyToManyField(DishIngredient, related_name='Генератор')

  def __str__(self):
      return f'{self.generator}'
  
  class Meta:
      verbose_name = 'Генератор Блюд'
      verbose_name_plural = 'Генератор Блюд'


class Favorite(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE, related_name='Сохраненное'
    )
    dish = models.ForeignKey(
        Dish, 
        on_delete=models.CASCADE, related_name='Сохраненное'
    )

    def __str__(self):
        return f'{self.owner} - {self.dish.title}'

    class Meta:
        verbose_name = 'Сохраненное'
        verbose_name_plural = 'Сохраненное'


class Comment(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE, related_name='comments'
    )
    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE, related_name='comments'
    )
    comment = models.TextField()
   
    def __str__(self):
        return f'{self.owner} - {self.dish}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'



