from django.db import models
from insurance_auth.models import User
from insurance_policy.models import Policy

# Create your models here.

class Payment(models.Model):
    
    id = models.AutoField(primary_key=True)
    card = models.IntegerField()
    cvv = models.IntegerField()
    date = models.DateField()

    # def __init__(self, card, cvv, date):
    #     super(Payment, self).__init__()
    #     self.card=card
    #     self.cvv=cvv
    #     self.date=date

    def __str__(self):
        return f'Payment {self.id}'


class UserPolicy(models.Model):

    id = models.AutoField(primary_key=True)
    policy_id = models.ForeignKey(Policy, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cost = models.IntegerField()
    payment = models.ForeignKey(Payment, on_delete=models.PROTECT)

    # def __init__(self, policy_id, user, cost, payment):
    #     super(UserPolicy, self).__init__()
    #     self.policy_id=policy_id
    #     self.user=user
    #     self.cost=cost
    #     self.payment=payment

    def __str__(self):
        return f'{self.user.email}, {self.policy_id.type}, {self.cost}'
    
