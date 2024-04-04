from django.urls import path
from .views import ImageListCreateAPIView, ImageRetrieveAPIView

urlpatterns = [
    path('images/', ImageListCreateAPIView.as_view(),),
    path('images/<int:pk>/', ImageRetrieveAPIView.as_view(),),
]
