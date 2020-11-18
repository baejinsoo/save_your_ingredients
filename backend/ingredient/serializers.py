from rest_framework import serializers
from ingredient.models import Ingredient
from django.contrib.auth.models import User


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = (
            'id',
            'name',
            'trim',
            'keep',
            'buy',
        )
        read_only_fields = ('id', 'name', 'trim', 'keep', 'buy', )

# class PostSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#     class Meta:
#         model = Post
#         fields = (
#             'id',
#             'title',
#             'subtitle',
#             'content',
#             'created_at',
#         )
#         read_only_fields = ('created_at',)
