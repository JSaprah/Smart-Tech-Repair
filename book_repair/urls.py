from . import views
from django.urls import path


urlpatterns = [
    path('booking/', views.phones_list, name='booking'),

    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
]
