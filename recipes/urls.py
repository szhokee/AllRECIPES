from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CuisineModelViewSet, IngredientModelViewSet, DishModelViewSet, FavoriteModelViewSet, CommentModelViewSet 

router = DefaultRouter()
router.register('', CuisineModelViewSet)
router.register('', IngredientModelViewSet)
router.register('', DishModelViewSet)
router.register('', FavoriteModelViewSet)
router.register('', CommentModelViewSet)

urlpatterns = [
    path('cuisines/', include(router.urls)),
    path('ingredients/', include(router.urls)),
    path('dishes/', include(router.urls)),
    path('favorites/', include(router.urls)),
    path('comments/', include(router.urls)),
]