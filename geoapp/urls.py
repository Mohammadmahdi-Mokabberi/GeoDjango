from django.urls import path

from .views import LocationAPIView, LocationDetailsAPIView,CreateLocationAPIView


urlpatterns = [
    path('location', LocationAPIView.as_view()),
    path('location/<str:pk>', LocationDetailsAPIView.as_view()),
    path('creat-location/',CreateLocationAPIView.as_view()),
]