from django.urls import path
from .views import ReviewListCreateAPIView, ReviewRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('reviews/', ReviewListCreateAPIView.as_view(),),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyAPIView.as_view(),),
]
