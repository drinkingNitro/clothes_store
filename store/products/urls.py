from django.urls import path

from products.views import ProductDetailsAPIView, ProductListAPIView

app_name = 'products'

urlpatterns = [
    path('', ProductListAPIView.as_view()),
    path('<int:pk>/', ProductDetailsAPIView.as_view()),
]
