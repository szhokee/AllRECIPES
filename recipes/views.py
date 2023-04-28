from rest_framework import generics
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Cuisine, Ingredient, Dish
from .serializers import CuisineSerializer, IngredientSerializer, DishSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter


class CustomPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000


class CuisineModelViewSet(ModelViewSet):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    

class IngredientModelViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']


class DishModelViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']






# class CustomPagination(PageNumberPagination):
#     page_size = 20
#     page_size_query_param = 'page_size'
#     max_page_size = 1000

# class CuisineList(generics.ListAPIView):
#     queryset = Cuisine.objects.all()
#     serializer_class = CuisineSerializer
#     pagination_class = CustomPagination
#     filter_backends = [SearchFilter]
#     filterset_fields = ['name']
#     search_fields = ['name']
    

# class IngredientList(generics.ListAPIView):
#     queryset = Ingredient.objects.all()
#     serializer_class = IngredientSerializer
#     pagination_class = CustomPagination
#     filter_backends = [SearchFilter]
#     filterset_fields = ['name']
#     search_fields = ['name']

# class DishList(generics.ListAPIView):
#     queryset = Dish.objects.all()
#     serializer_class = DishSerializer
#     pagination_class = CustomPagination
#     filter_backends = [SearchFilter]
#     filterset_fields = ['name']
#     search_fields = ['name']








