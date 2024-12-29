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
        phone_model = kwargs.pop('phone_model', None)
        super().__init__(*args, **kwargs)

        if phone_model:
            self.fields['phone_model'].initial = phone_model
            self.fields['phone_model'].queryset = Phonemodel.objects.filter(id=phone_model.id)
