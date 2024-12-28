from django import forms
from .models import Ticket, Phonemodel


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            "phonemodel",
            "broken_part",
            "issue_description",
            "imei"
            ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phonemodel'].queryset = Phonemodel.objects.all()
