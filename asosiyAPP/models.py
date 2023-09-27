from django.db import models
from django.conf import settings

# Create your models here.

class Bemor(models.Model):
    ism = models.CharField(max_length=50)
    manzil = models.CharField(max_length=150)
    tel = models.CharField(max_length=30)
    joylashgan = models.BooleanField(default=False)
    sana = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.ism

class Yollanma(models.Model):
    nom = models.CharField(max_length=30)
    qayerga = models.CharField(max_length=30)  # Example -->  Uzi, Laboratoriya, Doktor qabuli uchun
    narx = models.PositiveIntegerField()

    def __str__(self):
        return self.nom

class Tolov(models.Model):
    bemor = models.ForeignKey(Bemor, on_delete=models.SET_NULL, null=True)
    yollanma = models.ForeignKey(Yollanma,on_delete=models.CASCADE, null=True)
    sana = models.DateField(auto_now_add=True)
    tolandi = models.BooleanField(default=False)
    summa = models.PositiveIntegerField()
    tolangan_summa = models.JSONField(default=list())  # Example --> [{"sana":"2023-09-21","summa":150000}]
    haqdor = models.BooleanField(default=False)
    turi = models.CharField(max_length=30)
    joylashtirish = models.ForeignKey(settings.JOYLASH, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.bemor.ism} --> {self.yollanma.nom}"