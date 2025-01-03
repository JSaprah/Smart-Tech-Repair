from . import views
from django.urls import path


urlpatterns = [
    path('booking/', views.phones_list, name='booking'),
    path('booking/<slug:slug>/', views.create_ticket, name='create_ticket'),
    path(
        'confirmation/<str:ticket_number>',
        views.confirmation, name='confirmation'
        ),
    path('ticket_details/', views.ticket_details, name='ticket_details'),
    path('edit_ticket/<int:id>/', views.edit_ticket, name='edit_ticket'),
    path('account/', views.account, name='account'),
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
]
