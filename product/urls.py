from django.urls import path
from product import views


urlpatterns = [
    path('', views.ProductListAPIView.as_view(), name="products"),
    path('<int:id>', views.ProductDetailAPIView.as_view(), name="product"),
]
