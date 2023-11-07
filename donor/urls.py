from django.urls import path, include
from rest_framework.routers import SimpleRouter

from donor.views import DonorAllApplicationView, DonorCreateView, DonorPreviewForAllowed, DonorUpdateViewSet, \
    DonorDetailView, DonorUpdateView, DonorDeleteView

router = SimpleRouter()

router.register('', DonorUpdateViewSet, basename='update_donor')


urlpatterns = [
    path('create/', DonorCreateView.as_view()),
    path('list/', DonorAllApplicationView.as_view()),
    path('list-for-allowed/', DonorPreviewForAllowed.as_view()),
    path('detail/<int:pk>/', DonorDetailView.as_view()),
    path('update-application/<int:pk>/', DonorUpdateView.as_view()),
    path('delete-application/<int:pk>/', DonorDeleteView.as_view()),
    path('', include(router.urls)),
]

