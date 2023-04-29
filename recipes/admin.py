from django.contrib import admin
from .models import *


admin.site.register(Cuisine)
admin.site.register(Ingredient)
admin.site.register(Dish)
admin.site.register(DishIngredient)
admin.site.register(Favorite)