from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# schema_view = get_schema_view(
#    openapi.Info(
#       title='Movie Matching API',
#       default_version='v1',
#       description='Документация для проекта рекомендательной системы киносервиса.',
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )


urlpatterns = [
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', 
    #    schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), 
    #     name='schema-swagger-ui'),
    # re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), 
    #     name='schema-redoc'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
