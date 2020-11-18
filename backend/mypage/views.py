from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserDetailSerializer, ExperienceRecipeSerializer
from .models import UserDetail, ExperienceRecipe
from recipe.models import Recipe
from rest_framework import permissions
from django.shortcuts import get_object_or_404
# Create your views here.


class UserDetailView(APIView):
    def get(self, request):
        try:
            print("1")
            # user_detail = get_object_or_404(UserDetail, user=request.user)
            user_detail = UserDetail.objects.get(user=request.user)
        except:
            print("2")
            user_detail = UserDetail()
            user_detail.user = request.user
            user_detail.total_time = 0
            user_detail.save()
            # user_detail = UserDetail.objects.get(user=request.user)
        print("3")
        print(user_detail)
        serializer = UserDetailSerializer(user_detail)
        # print(serializer.data)
        return Response(serializer.data)


class WishRecipeView(APIView):
    def get(self, request):
        user_detail = UserDetail.objects.get(user=request.user)
        wish_recipes = user_detail.wish_recipes.all()
        print(wish_recipes)
        wish_recipes_list = []
        for wish in wish_recipes:
            wish_recipes_list.append(wish.reci_id)
        print(wish_recipes_list)
        return Response(wish_recipes_list)

    def post(self, request):
        data = request.data
        reci_id = data['reci_id']
        user_detail = UserDetail.objects.get(user=request.user)
        recipe = Recipe.objects.get(reci_id=reci_id)
        user_detail.wish_recipes.add(recipe)
        
        wish_recipes = user_detail.wish_recipes.all()
        print(wish_recipes)
        wish_recipes_list = []
        for wish in wish_recipes:
            wish_recipes_list.append(wish.reci_id)
        print(wish_recipes_list)
        return Response(wish_recipes_list)

    def delete(self, request):
        data = request.data
        reci_id = data['reci_id']
        user_detail = UserDetail.objects.get(user=request.user)
        recipe = Recipe.objects.get(reci_id=reci_id)
        user_detail.wish_recipes.remove(recipe)

        wish_recipes = user_detail.wish_recipes.all()
        print(wish_recipes)
        wish_recipes_list = []
        for wish in wish_recipes:
            wish_recipes_list.append(wish.reci_id)
        print(wish_recipes_list)
        return Response(wish_recipes_list)


class ExperienceRecipeView(APIView):
    def get(self, request):
        user_detail = UserDetail.objects.get(user=request.user)
        experience_recipe = user_detail.experiencerecipe.all()
        serializer = ExperienceRecipeSerializer(experience_recipe, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        reci_id = data['reci_id']
        user_detail = UserDetail.objects.get(user=request.user)
        recipe = get_object_or_404(Recipe, reci_id=reci_id)
        user_detail.wish_recipes.remove(recipe)

        experience_recipe = ExperienceRecipe()
        experience_recipe.recipe = recipe
        experience_recipe.user_detail = user_detail
        experience_recipe.save()

        user_detail.total_time += 30
        user_detail.save()
        
        serializer = ExperienceRecipeSerializer(experience_recipe)
        return Response(serializer.data)