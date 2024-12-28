from django.contrib import admin
from .models import Ticket, Service, Phonemodel, Part
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Ticket)
class PostAdmin(SummernoteModelAdmin):

    list_display = (
        'ticket_number',
        'imei',
        'phonemodel',
        'broken_part',
        'booking_date',
        'issue_description',
        'status',
        'created_on'
        )
    readonly_fields = ['ticket_number']
    search_fields = [
        'phonemodel__make__icontains',
        'phonemodel__series',]
    list_filter = (
        'status',
        'phonemodel__manufacturer',
        'booking_date'
        )
    # prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('issue_description',)


# Register your models here.
admin.site.register(Service)
admin.site.register(Phonemodel)
admin.site.register(Part)
