from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.permissions import OR, IsAdminUser
from .models import DonorApplication
from .serializers import DonorRegisterSerializer, DonorListSerializer, DonorListForAllowed
from account.permissions import IsOwnerOrAdmin, IsAdminOrAllowedPerson


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


class DonorUpdateViewSet(viewsets.ModelViewSet):
    serializer_class = DonorRegisterSerializer
    permission_classes = [IsOwnerOrAdmin, ]

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)

    @action(detail=False, methods=['PATCH'])
    def update_my_application(self, request):
        if self.request.user.is_anonymous:
            raise AuthenticationFailed("You are not authenticated. Please provide a valid token.")

        # Поиск анкеты пользователя на основе информации из токена
        user = self.request.user
        donor_application = DonorApplication.objects.filter(user_email=user).first()

        if not donor_application:
            return Response({"detail": "Donor application not found for the user."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(donor_application, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def my_application(self, request):
        if self.request.user.is_anonymous:
            raise AuthenticationFailed("You are not authenticated. Please provide a valid token.")
        user = self.request.user
        donor_application = DonorApplication.objects.filter(user_email=user).first()

        if not donor_application:
            return Response({'detail': 'Donor application not found for the user'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = DonorListSerializer(donor_application)
        return Response(serializer.data)

    http_method_names = ['patch', 'get']
