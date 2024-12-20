from django.contrib import admin
from .models import Customer, Ticket, Service, Phonemodel
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Ticket)
class PostAdmin(SummernoteModelAdmin):

    list_display = (
        'booking_date',
        'customer',
        'imei',
        'issue_description',
        'status',
        'phonemodel',
        'broken_part',
        'created_on'
        )
    search_fields = [
        'phonemodel__make__icontains',
        'customer__first_name__icontains',
        'customer__last_name__icontains']
    list_filter = (
        'status', 
        'phonemodel__manufacturer',
        )
    # prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('issue_description',)


# Register your models here.
admin.site.register(Customer)
# admin.site.register(Ticket)
admin.site.register(Service)
admin.site.register(Phonemodel)