from django.contrib import admin
from .models import Customer, Device, Ticket, Service, Phonemodel

# Register your models here.
admin.site.register(Customer)
admin.site.register(Device)
admin.site.register(Ticket)
admin.site.register(Service)
admin.site.register(Phonemodel)
