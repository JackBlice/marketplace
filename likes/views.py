from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Like
from .serializers import LikeSerializer

class LikeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LikeRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
