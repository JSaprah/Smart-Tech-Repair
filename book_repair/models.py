from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Pending"), (1, "In progress"), (2, "Completed"))
MANUFACTURER = ((0, "Apple"), (1, "Samsung"))
MAKE = ("")
REPAIR_DURATION = 1
PART = (
    (1, "Diagnostic Services"),
    (2, "Screen Replacement"),
    (3, "Battery Replacement"),
    (4, "Charging port Replacement"),
    (5, "Headphone Jack Repair"),
    (6, "Microphone Repair"),
    (7, "Loudspeaker Repair"),
    (8, "Speaker Repair"),
    (9, "Rear Camera Repair"),
    (10, "Front Camera Repair"),
    (11, "Backglass Repair"),
    (12, "Rear housing Replacement"),
)


# Create your models here.
class Device(models.Model):
    manufacturer = models.IntegerField(choices=MANUFACTURER)
    make = models.IntegerField(choices=MAKE)


class Part(models.Model):
    device_part = models.TextField(choices=PART)


class Customer(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=False)


class Catalogue(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    device_part = models.ForeignKey(Part, on_delete=models.CASCADE)
    price = models.CharField()


class Ticket(models.Model):
    ticketnumber = models.AutoField(primary_key=True, editable=False)
    imei = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    booking_date = models.DateTimeField()
    duration = models.IntegerField(REPAIR_DURATION)
    damage = models.ForeignKey(Part, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
