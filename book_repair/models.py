from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Pending"), (1, "In progress"), (2, "Completed"))
MANUFACTURER = ((0, "Apple"), (1, "Samsung"))
MAKE = ("")
REPAIR_DURATION = 1
PART = (
    "Diagnostic Services",
    "Screen Replacement",
    "Battery Replacement",
    "Charging port Replacement",
    "Headphone Jack Repair",
    "Microphone Repair",
    "Loudspeaker Repair",
    "Speaker Repair",
    "Rear Camera Repair",
    "Front Camera Repair",
    "Backglass Repair",
    "Rear housing Replacement"
)


# Create your models here.
class device(models.Model):
    manufacturer = models.IntegerField(choices=MANUFACTURER)
    make = models.IntegerField(choices=MAKE)


class part(models.Model):
    device_part = models.Choices(PART)


class customer(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=False)


class catalogue(models.Models):
    device = models.ForeignKey(device, on_delete=models.CASCADE)
    device_part = models.ForeignKey(part, on_delete=models.CASCADE)
    price = models.CharField()


class ticket(models.Model):
    ticketnumber = models.AutoField(primary_key=True, editable=False)
    imei = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    booking_date = models.DateTimeField()
    duration = models.IntegerField(REPAIR_DURATION)
    damage = models.ForeignKey(part, on_delete=models.CASCADE)
    device = models.ForeignKey(device, on_delete=models.CASCADE)
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
