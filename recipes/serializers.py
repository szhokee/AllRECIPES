from rest_framework import serializers
from .models import Cuisine, Ingredient, Dish, DishIngredient

class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class DishIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()
    class Meta:
        model = DishIngredient
        fields = ('ingredient', 'quantity')

class DishSerializer(serializers.ModelSerializer):
    cuisine = CuisineSerializer()
    ingredients = DishIngredientSerializer(many=True)
    class Meta:
        model = Dish
        fields = '__all__'