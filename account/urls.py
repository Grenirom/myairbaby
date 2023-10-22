from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views
from account.views import LoginView, RefreshView, UserRegisterView, UserProfileViewSet, ApproveSellerView

router = SimpleRouter()
router.register(r'', UserProfileViewSet, basename='accounts')

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('refresh/', RefreshView.as_view()),
    path('login/', LoginView.as_view()),
    path('user-all/', views.AllUsersView.as_view()),
    path('approve-person/', ApproveSellerView.as_view()),
    path('', include(router.urls)),
    # path('user-update/<int:pk>/', views.UserUpdate.as_view()),
]
