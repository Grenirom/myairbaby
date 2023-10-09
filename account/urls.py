from django.urls import path

from account.views import LoginView, RefreshView, UserRegisterView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('refresh/', RefreshView.as_view()),
    path('login/', LoginView.as_view()),
]
