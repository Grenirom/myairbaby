from django.urls import path, include
from rest_framework.routers import DefaultRouter

from donor.views import DonorRegisterView

urlpatterns = [
    path('create/', DonorRegisterView.as_view()),

]
