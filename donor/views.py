from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets, status, generics
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from .models import DonorApplication
from .serializers import DonorRegisterSerializer, DonorListSerializer, DonorListForAllowed
from account.permissions import IsOwnerOrAdmin, IsAdminOrAllowedPerson

from rest_framework_simplejwt.authentication import JWTAuthentication
User = get_user_model()


class DonorAllApplicationView(generics.ListAPIView):
    queryset = DonorApplication.objects.all()
    serializer_class = DonorListSerializer
    permission_classes = [permissions.IsAdminUser, ]


class DonorCreateView(generics.CreateAPIView):
    queryset = DonorApplication.objects.all()
    serializer_class = DonorRegisterSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def perform_create(self, serializer):
        user_email = self.request.user.email
        user = User.objects.get(email=user_email)
        serializer.save(user_email=user)


class DonorPreviewForAllowed(generics.ListAPIView):
    serializer_class = DonorListForAllowed
    permission_classes = [IsAdminOrAllowedPerson, ]

    def get_queryset(self):
        if self.request.user.is_anonymous and not self.request.user.is_allowed:
            raise AuthenticationFailed("You are not authenticated. Please provide a valid token.")
        return DonorApplication.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)
