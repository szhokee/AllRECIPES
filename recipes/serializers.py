from rest_framework import serializers
from .models import Cuisine, Ingredient, Dish, DishIngredient, Favorite, Comment

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

class FavoriteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    
    class Meta:
        model = Favorite
        fields = '__all__' 


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'