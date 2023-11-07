from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from .models import DonorApplication
from .serializers import DonorRegisterSerializer, DonorListSerializer, DonorListForAllowed, DonorUpdateSerializer
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
        serializer.save(user=user)


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

    @action(detail=False, methods=['GET'])
    def my_applications(self, request):
        if self.request.user.is_anonymous:
            raise AuthenticationFailed("Вы не авторизованы. Пожалуйста, предоставьте действительный токен.")

        user = self.request.user
        donor_applications = DonorApplication.objects.filter(user_email=user).all()

        if not donor_applications:
            return Response({'detail': 'Заявка донора не найдена для данного пользователя'},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = DonorListSerializer(donor_applications, many=True)
        return Response(serializer.data)

    http_method_names = ['patch', 'get']


class DonorDetailView(generics.RetrieveAPIView):
    queryset = DonorApplication.objects.all()
    serializer_class = DonorListSerializer
    permission_classes = [IsOwnerOrAdmin, ]


class DonorUpdateView(generics.UpdateAPIView):
    queryset = DonorApplication.objects.all()
    serializer_class = DonorUpdateSerializer
    permission_classes = [IsOwnerOrAdmin, ]


class DonorDeleteView(generics.DestroyAPIView):
    queryset = DonorApplication.objects.all()
    permission_classes = [IsOwnerOrAdmin, ]