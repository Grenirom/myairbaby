from rest_framework import permissions, generics
from .models import DonorApplication
from .serializers import DonorRegisterSerializer
from account.permissions import IsOwnerOrAdmin


class DonorRegisterView(generics.CreateAPIView):
    queryset = DonorApplication.objects.all()
    serializer_class = DonorRegisterSerializer

    def get_permissions(self):
        if self.request.user.is_superuser:
            return (permissions.IsAdminUser(), )
        return (permissions.IsAuthenticated(), )




