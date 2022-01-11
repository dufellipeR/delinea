from django.contrib import admin
from django.urls import path, include
from product import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Delinea Docs",
      default_version='v1',
      description="Backend Teste",
      terms_of_service="None",
      contact=openapi.Contact(email="eduardo.fellipe30@gmail.com"),
      license=openapi.License(name="None"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',  include('authentication.urls')),
    path('social_auth/', include(('social_auth.urls', 'social_auth'),
                                 namespace="social_auth")),
    path('product/', include('product.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('api/api.json', schema_view.without_ui(cache_timeout=0), name='schema-swagger-ui'),

    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    

]
