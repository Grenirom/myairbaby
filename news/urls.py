from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('', views.NewViewSet, basename='new_router')

urlpatterns = [
    path('create/', views.NewCreateView.as_view()),
    path('', include(router.urls)),

]
