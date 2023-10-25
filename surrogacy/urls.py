from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('', views.SurrogacyMyApplicationViewSet, basename='surrogacy-application')

urlpatterns = [
    path('create-application/', views.SurrogacyCreateView.as_view()),
    path('admin-list/', views.SurrogacyAdminListView.as_view()),
    path('', include(router.urls)),

]
