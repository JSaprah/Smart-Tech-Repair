from . import views
from django.urls import path


urlpatterns = [
    path('booking/', views.phones_list, name='booking'),
    path('booking/<slug:slug>/', views.create_ticket, name='create_ticket'),
    path('new_customer/', views.create_customer, name='new_customer'),
    path('ticket_details/', views.ticket_details, name='ticket_details'),
    path('edit_ticket/<int:id>/', views.edit_ticket, name='edit_ticket'),
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
]
