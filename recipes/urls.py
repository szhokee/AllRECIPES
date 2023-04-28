from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CuisineModelViewSet, IngredientModelViewSet, DishModelViewSet 

router = DefaultRouter()
router.register('', CuisineModelViewSet)
router.register('', IngredientModelViewSet)
router.register('', DishModelViewSet)

urlpatterns = [
    path('cuisines/', include(router.urls)),
    path('ingredients/', include(router.urls)),
    path('dishes/', include(router.urls)),
]