from django.db import models

from asosiyAPP.models import Bemor


# Create your models here.

class Xona(models.Model):
    qavat = models.PositiveIntegerField()
    raqam = models.PositiveIntegerField()
    sigim = models.PositiveIntegerField()
    bosh_joy_soni = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.qavat} -- {self.raqam}"

class Joylashtirish(models.Model):
    bemor = models.ForeignKey(Bemor, on_delete=models.CASCADE)
    xona = models.ForeignKey(Xona, on_delete=models.CASCADE)
    kelish_sana = models.DateField()
    ketish_sana = models.DateField(null=True,blank=True)
    qarovchi = models.BooleanField(default=False)