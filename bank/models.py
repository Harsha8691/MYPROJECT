
from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=255)

class Branch(models.Model):
    bank = models.ForeignKey(Bank, related_name='branches', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

