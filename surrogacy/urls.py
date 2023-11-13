from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views
from .views import SurrogacyUpdateView

router = SimpleRouter()
router.register('', views.SurrogacyMyApplicationViewSet, basename='surrogacy-application')

urlpatterns = [
    path('create-application/', views.SurrogacyCreateView.as_view()),
    path('admin-list/', views.SurrogacyAdminListView.as_view()),
    path('admin-detail/<int:pk>/', views.SurrogacyAdminDetailView.as_view()),
    path('update-application/<int:pk>/', SurrogacyUpdateView.as_view()),
    path('delete-application/<int:pk>/', views.SurrogacyDeleteView.as_view()),
    path('', include(router.urls)),

]
