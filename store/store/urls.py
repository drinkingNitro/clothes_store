"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from products.views import ProductListAPIView, ProductDetailsAPIView
from users.views import UserCreateAPIView, FavoriteModelViewSet
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', ProductListAPIView.as_view()),
    path('api/products/<int:pk>/', ProductDetailsAPIView.as_view()),
    path('api/users/create/', UserCreateAPIView.as_view()),
    path('api/obtain_auth_token/', obtain_auth_token),
    path('api/users/favorite/', FavoriteModelViewSet.as_view({'get': 'list'})),
    path('api/users/add_favorite/<int:pk>/', FavoriteModelViewSet.as_view({'post': 'create'})),
    path('api/users/favorite/<int:pk>/', FavoriteModelViewSet.as_view({'delete': 'destroy'})),
]
