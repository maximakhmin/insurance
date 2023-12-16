from .models import Policy, Payment, UserPolicy





def purchase(type, id, request):
    policy = Policy.objects.get(id=id)
    if (policy.type !=type):
        raise Exception("Incorrect type")
    data = {
        'card': request.data.get('card'),
        'cvv': request.data.get('cvv'),
        'date': request.data.get('date'),
    }

    payment = Payment.objects.filter(card=data['card'], cvv=data['cvv'], date=data['date']).first()
    if not payment:
        payment = Payment()
        payment.card=data['card']
        payment.cvv=data['cvv']
        payment.date=data['date']
        payment.save()

    userPolicy = UserPolicy()
    userPolicy.policy_id=policy
    userPolicy.user=request.user
    userPolicy.cost=request.user.current_cost
    userPolicy.payment=payment
    userPolicy.save()


KM = {
    0: 0.6,
    50: 1,
    70: 1.1,
    100: 1.2,
    120: 1.4,
    150: 1.6
}

KBC = {
    16: {0:1.87, 3:1.66},
    22: {0:1.77, 3:1.04},
    25: {0:1.77, 1:1.69, 2:1.63, 3:1.04, 10:1.01},
    30: {0:1.63, 3:1.04, 7:1.01, 10:0.96},
    35: {0:1.63, 3:0.99, 5:0.96},
    40: {0:1.63, 3:0.96},
    50: {0:1.63, 3:0.96},
    59: {0:1.60, 3:0.93}
}

def calculateCoef(data):
    km = 0
    for elem in KM.keys():
        if data['power'] > elem:
            km = KM[elem]

    kbc = 0
    for elem1 in KBC.keys():
        if data['age']>elem1:
            for elem2 in KBC[elem1].keys():
                if data['experiance']>elem2:
                    kbc = KBC[elem1][elem2]
    
    ko = 1
    if (data['user_limit'])==True:
        ko = 2.22

    return km*kbc*ko
    


