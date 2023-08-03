from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from users.models import User, Favorite
from users.serializers import UserSerializer, FavoriteSerializer
from rest_framework.viewsets import ModelViewSet
from users.permissions import IsOwner


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FavoriteModelViewSet(ModelViewSet):
    serializer_class = FavoriteSerializer
    def get_permissions(self):
        if self.action in ('list', 'create'):
            self.permission_classes = (IsAuthenticated,)
        elif self.action == 'destroy':
            self.permission_classes = (IsOwner,)
        return super().get_permissions()

    def get_queryset(self):
        if self.request.user.id:
            return Favorite.objects.filter(user=self.request.user)
        return {}
    #
    def create(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = Product.objects.get(id=product_id)
        user = request.user
        serializer = FavoriteSerializer(data={'user': user, "product": product})
        serializer.is_valid(raise_exception=True)
        serializer.save(product=product, user=user)
        product.increase_product_rate()
        product.save()
        return Response({'favorite': serializer.data})
    #
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        product = instance.product
        instance.delete()
        product.decrease_product_rate()
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
