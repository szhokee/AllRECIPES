from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title = 'AllRECIPES',
        default_version = 'v1',
        description = 'Web-Site'
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('swagger/', schema_view.with_ui('swagger')),
]
