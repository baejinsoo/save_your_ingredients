from rest_framework import serializers
from mypage.models import UserDetail, ExperienceRecipe
from recipe.serializers import RecipeSerializer
from django.contrib.auth.models import User
from recipe.models import Recipe

class ExperienceRecipeSerializer(serializers.ModelSerializer):
    reci_id = serializers.ReadOnlyField(source='recipe.reci_id')
    class Meta:
        model = ExperienceRecipe
        exclude = ('user_detail', )
        # fields = ("id", "recipe", "created_date", )
        # field = "__all__"
        read_only_fields = ('id', )


class UserDetailSerializer(serializers.ModelSerializer):
    wish_recipes = RecipeSerializer(many=True, required=False)
    experience_recipes = ExperienceRecipeSerializer(
        source='experiencerecipe', many=True)

    class Meta:
        model = UserDetail
        fields = ('user', 'wish_recipes',
                  'experience_recipes', 'total_time', )
        read_only_fields = ('id', )
