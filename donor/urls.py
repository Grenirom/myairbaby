from django.urls import path, include
from rest_framework.routers import SimpleRouter

from donor.views import DonorAllApplicationView, DonorCreateView, DonorPreviewForAllowed, DonorUpdateViewSet

router = SimpleRouter()

router.register('', DonorUpdateViewSet, basename='update_donor')


urlpatterns = [
    path('list/', DonorAllApplicationView.as_view()),
    path('create/', DonorCreateView.as_view()),
    path('list-for-allowed/', DonorPreviewForAllowed.as_view()),
    path('', include(router.urls)),
]

