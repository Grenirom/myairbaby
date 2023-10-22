from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import generics, permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .permissions import IsOwnerOrAdmin
from .serializers import RegisterSerializer

User = get_user_model()


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class AllUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser, )


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrAdmin, ]

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)  # Фильтруем по текущему пользователю

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())  # Применяем фильтры
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        user_instance = self.get_object()

        try:
            user_profile_instance = User.objects.get(user=user_instance)
            serializer = self.get_serializer(user_profile_instance)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"detail": "Profile does not exist"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['PUT', 'PATCH'])
    def update_my_profile(self, request):
        profile = self.request.user
        if self.request.user.is_anonymous:
            raise AuthenticationFailed("You are not authenticated. Please provide a valid token.")
        serializer = self.get_serializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, methods=['DELETE'])
    def delete_my_profile(self, request):
        current_user = request.user

        if current_user.is_anonymous:
            raise AuthenticationFailed("You are not authenticated. Please provide a valid token.")
        current_user.delete()

        return Response({'msg': 'Account deleted'}, status=204)


class ApproveSellerView(APIView):
    permission_classes = [permissions.IsAdminUser, ]

    def post(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"message": "User not found."},
                            status=status.HTTP_404_NOT_FOUND)

        if not user.is_allowed:
            return Response({"message": "Application was not found!"}, status=status.HTTP_400_BAD_REQUEST)

        user.is_allowed = True
        user.save()

        return Response({"message": "Seller approved."}, status=status.HTTP_200_OK)


class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)


class RefreshView(TokenRefreshView):
    permission_classes = (permissions.AllowAny,)
