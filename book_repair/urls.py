from . import views
from django.urls import path


urlpatterns = [
    path('booking/', views.phones_list, name='booking'),
    path('booking/<booking>/', views.booking_details, name='booking_details'),
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
]
