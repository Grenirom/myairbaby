from requests import Response
from rest_framework import generics, permissions, viewsets

from .mixins import RatingMixin, CommentMixin
from .models import New
from .serializers import NewCreateSerializer, NewSerializer


class NewCreateView(generics.CreateAPIView):
    queryset = New.objects.all()
    serializer_class = NewCreateSerializer
    permission_classes = [permissions.IsAdminUser,]


class NewViewSet(viewsets.ModelViewSet, RatingMixin, CommentMixin):
    queryset = New.objects.all()
    serializer_class = NewSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAdminUser(), ]
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated(), ]
        elif self.request.method == 'GET':
            return [permissions.AllowAny(), ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    http_method_names = ['get', 'post']
