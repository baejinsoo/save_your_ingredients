from rest_framework import serializers
from stock.models import Stock
from django.contrib.auth.models import User


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
        read_only_fields = ('id', )