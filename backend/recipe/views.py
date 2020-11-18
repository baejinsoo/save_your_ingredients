from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RecipeSerializer
from .recommend_recipe import recommend_ingredient, recommend_expiration_date, recommend_random
from stock.models import Stock


class RecipeExpirationAPIView(APIView):
    serializer_class = RecipeSerializer

    def get(self, request, *args, **kwargs):
        queryset = Stock.objects.filter(user_id=request.user.id)
        result_dict = recommend_expiration_date(queryset)
        print(result_dict)
        return Response(result_dict)


class RecipeStockAPIView(APIView):
    serializer_class = RecipeSerializer

    def get(self, request, *args, **kwargs):
        queryset = Stock.objects.filter(user_id=request.user.id)
        result_dict = recommend_ingredient(queryset)
        return Response(result_dict)


class RandomAPIView(APIView):
    serializer_class = RecipeSerializer

    def get(self, request, *args, **kwargs):
        result_dict = recommend_random()
        print(result_dict)
        return Response(result_dict)