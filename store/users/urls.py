from django.urls import include, path

from users.views import FavoriteModelViewSet, UserCreateAPIView

app_name = 'users'

urlpatterns = [
    path('create/', UserCreateAPIView.as_view()),
    path('favorite/', FavoriteModelViewSet.as_view({'get': 'list'})),
    path('add_favorite/<int:pk>/', FavoriteModelViewSet.as_view({'post': 'create'})),
    path('favorite/<int:pk>/', FavoriteModelViewSet.as_view({'delete': 'destroy'})),
]
