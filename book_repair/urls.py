from . import views
from django.urls import path


urlpatterns = [
    path('booking/', views.phones_list, name='booking'),
    path('booking/<int:id>/', views.create_ticket, name='create_ticket'),
    path('ticket_details/', views.login, name='ticket_details'),
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
]
