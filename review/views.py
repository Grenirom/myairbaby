from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from .models import Review
from .serializers import ReviewCreateSerializer, ReviewUpdateSerializer
from account.permissions import IsOwnerOrAdmin

User = get_user_model()


class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def perform_create(self, serializer):
        user_email = self.request.user.email
        user = User.objects.get(email=user_email)
        serializer.save(user=user)


class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = [permissions.AllowAny, ]


class ReviewUpdateView(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_claszs = ReviewUpdateSerializer
    permission_classes = [IsOwnerOrAdmin, ]


class ReviewDeleteView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    permission_classes = [IsOwnerOrAdmin, ]

