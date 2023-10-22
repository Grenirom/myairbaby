from django.urls import path, include

from donor.views import DonorAllApplicationView, DonorCreateView, DonorPreviewForAllowed

urlpatterns = [
    path('list/', DonorAllApplicationView.as_view()),
    path('create/', DonorCreateView.as_view()),
    path('list-for-allowed/', DonorPreviewForAllowed.as_view()),
]
