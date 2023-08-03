from rest_framework import serializers

from users.models import Favorite, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email',)

    # for correct save to db (with hashed password)
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    product = serializers.SlugRelatedField(slug_field='id', read_only=True)

    class Meta:
        model = Favorite
        fields = ('id', 'user', 'product',)
