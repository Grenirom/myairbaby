from django.contrib.auth import get_user_model
from rest_framework import permissions, generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from account.permissions import IsOwnerOrAdmin
from .models import Surrogacy
from .serializers import SurrogacyCreateSerializer, SurrogacyAdminListSerializer, SurrogacyUpdateSerializer

User = get_user_model()


class SurrogacyCreateView(generics.CreateAPIView):
    queryset = Surrogacy.objects.all()
    serializer_class = SurrogacyCreateSerializer
    permission_classes = [permissions.IsAdminUser | permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user_email = self.request.user.email
        user = User.objects.get(email=user_email)
        serializer.save(owner_email=user)


class SurrogacyAdminListView(generics.ListAPIView):
    queryset = Surrogacy.objects.all()
    serializer_class = SurrogacyAdminListSerializer
    permission_classes = [permissions.IsAdminUser, ]


class SurrogacyMyApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = SurrogacyAdminListSerializer
    permission_classes = [IsOwnerOrAdmin, ]

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return SurrogacyUpdateSerializer

    @action(detail=False, methods=['PATCH'])
    def update_my_application(self, request):
        if self.request.user.is_anonymous:
            raise AuthenticationFailed("You are not authenticated. Please provide a valid token.")

        # Поиск анкеты пользователя на основе информации из токена
        user = self.request.user
        surrogacy_application = Surrogacy.objects.filter(owner_email=user).first()

        if not surrogacy_application:
            return Response({"detail": "Surrogacy application not found for the user."},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(surrogacy_application,
                                         data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def my_application(self, request):
        if self.request.user.is_anonymous:
            raise AuthenticationFailed("You are not authenticated. Please provide a valid token.")
        user = self.request.user
        sur_application = Surrogacy.objects.filter(owner_email=user).first()

        if not sur_application:
            return Response({'detail': 'Surrogacy application not found for the user'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = SurrogacyAdminListSerializer(sur_application)
        return Response(serializer.data)

    http_method_names = ['patch', 'get']
