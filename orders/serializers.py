from rest_framework import serializers
from .models import Order
from products.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'products', 'created_at']
