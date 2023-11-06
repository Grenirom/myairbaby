from django.urls import path
from . import views

urlpatterns = [
    path('create-review/', views.ReviewCreateView.as_view()),
    path('list-review/', views.ReviewListView.as_view()),
    path('update-review/<int:pk>/', views.ReviewUpdateView.as_view()),
    path('delete-review/<int:pk>/', views.ReviewDeleteView.as_view()),
]
