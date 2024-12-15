from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Pending"), (1, "In progress"), (2, "Completed"))
TYPE = ((0, "Phone"), (1, "Laptop"), (2, "Tablet"))
MANUFACTURER = (
    (0, "Apple"),
    (1, "Samsung"),
    (2, "Google"),
    (3, "HP"),
    (4, "Dell")
    )
MAKE = ((0, "11"), (1, 12), (2, 13), (3, 14), (4, 15))


# Create your models here.
class job_request(models.Model):
    description = models.TextField
    status = models.IntegerField(choices=STATUS, default=0)


class repairtypes(models.Model):
    repair_type = models.IntegerField(choices=TYPE)


class device(models.Model):
    repair_type = models.ForeignKey(repairtypes, on_delete=models.CASCADE)
    imei = models.CharField(max_length=200)
    manufacturer = models.IntegerField(choices=MANUFACTURER)
    make = models.IntegerField(choices=MAKE)


class customer(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    request = models.ForeignKey(job_request, on_delete=models.CASCADE)
