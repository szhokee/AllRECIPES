from rest_framework import generics
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Cuisine, Ingredient, Dish, Favorite, Comment, Generator
from .serializers import CuisineSerializer, IngredientSerializer, DishSerializer, FavoriteSerializer, CommentSerializer, GeneratorSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from collections import defaultdict


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


class GeneratorModelViewSet(ModelViewSet):
    queryset = Generator.objects.all()
    serializer_class = GeneratorSerializer
    permission_classes = [IsAuthenticated]

    def findAllRecipes(self, recipes, ingredients, supplies):
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for r,ing in zip(recipes,ingredients):
            for i in ing:
                graph[i].append(r)
                in_degree[r]+=1

        queue = supplies[::]
        res = []
        while queue:
            ing = queue.pop(0)
            if ing in recipes:
                res.append(ing)

            for child in graph[ing]:
                in_degree[child]-=1
                if in_degree[child]==0:
                    queue.append(child)

        return res


class FavoriteModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)






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








