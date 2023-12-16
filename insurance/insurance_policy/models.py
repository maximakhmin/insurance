from django.db import models

# Create your models here.

class Policy(models.Model):

    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    cost = models.IntegerField()
    payment = models.IntegerField()
    description = models.CharField(max_length=511)
    active = models.BooleanField(default=True)

    def __str__(self):
        return (f'Тип полиса: {self.type}, цена полиса: {self.cost}, цена выплат: {self.payment}')