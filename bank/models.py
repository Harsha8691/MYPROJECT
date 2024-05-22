from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=100)
    established_date = models.DateField()

    def __str__(self):
        return self.name

class Branch(models.Model):
    bank = models.ForeignKey(Bank, related_name='branches', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

