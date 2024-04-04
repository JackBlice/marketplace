# В файле urls.py в приложении "favorites"

from django.urls import path
from .views import FavoriteItemListCreateAPIView, FavoriteItemRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('favorites/', FavoriteItemListCreateAPIView.as_view(), name='favorite-list-create'),
    path('favorites/<int:pk>/', FavoriteItemRetrieveUpdateDestroyAPIView.as_view(), name='favorite-detail'),
]
