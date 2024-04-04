# В файле serializers.py в приложении "favorites"

from rest_framework import serializers
from .models import FavoriteItem

class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = ['id', 'user', 'product', 'created_at']
