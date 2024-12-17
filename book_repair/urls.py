from . import views
from django.urls import path

urlpatterns = [
    path('booking/', views.booking.as_view(), name='booking'),
]
