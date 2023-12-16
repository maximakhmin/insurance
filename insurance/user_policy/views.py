from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserPolicy, Payment, Policy, User
from insurance_policy.serializer import PolicySerializer
from .serializer import UserPolicySerializer
from .purchase import purchase, calculateCoef
# Create your views here.
        
    
@api_view(('GET',)) 
def getIndex(request):
    return Response("index")
    
@api_view(('GET',)) 
def getAuto(request):
    policies = Policy.objects.filter(type='auto', active=True)
    serializer = PolicySerializer(policies, many=True)
    return Response(serializer.data)

@api_view(('GET',)) 
def getAccident(request):
    policies = Policy.objects.filter(type='accident', active=True)
    serializer = PolicySerializer(policies, many=True)
    return Response(serializer.data)

@api_view(('GET',)) 
def getPropetry(request):
    policies = Policy.objects.filter(type='property', active=True)
    serializer = PolicySerializer(policies, many=True)
    return Response(serializer.data)

@api_view(('POST',)) 
def calculateAuto(request, id):
    try:
        policy = Policy.objects.filter(type='auto').get(id=id)

        data = {
            'power': request.data.get('power'),
            'user_limit': request.data.get('user_limit'),
            'age': request.data.get('age'),
            'experiance': request.data.get('experiance'),
        }

        cost = policy.cost * calculateCoef(data)
        request.user.current_cost = cost
        request.user.save()

        return Response(f'Cost of insurance: {cost}')
        
    except Policy.DoesNotExist:
        return Response("No such id")
    except Exception as e:
        print(e)
        return Response("Error")

@api_view(('POST',)) 
def buyAuto(request, id):
    try:
        purchase('auto', id, request)

        request.user.current_cost = 0
        request.user.save()

        return Response("Insurance bought")
    except Policy.DoesNotExist:
        return Response("No such id")
    except Exception as e:
        print(e)
        return Response("Error")

@api_view(('POST',)) 
def buyAccident(request, id):
    try:
        policy = Policy.objects.filter(type='accident').get(id=id)

        request.user.current_cost = policy.cost
        request.user.save()

        purchase('accident', id, request)

        request.user.current_cost = 0
        request.user.save()

        return Response("Insurance bought")
    except Policy.DoesNotExist:
        return Response("No such id")
    except Exception as e:
        print(e)
        return Response("Error")


@api_view(('POST',)) 
def buyPropetry(request, id):
    try:
        policy = Policy.objects.filter(type='property').get(id=id)

        request.user.current_cost = policy.cost
        request.user.save()

        purchase('property', id, request)

        request.user.current_cost = 0
        request.user.save()

        return Response("Insurance bought")
    except Policy.DoesNotExist:
        return Response("No such id")
    except Exception as e:
        print(e)
        return Response("Error")
    

@api_view(('GET',)) 
def getPolicies(request):
    userPolicies = UserPolicy.objects.filter(user=request.user)
    serializer = UserPolicySerializer(userPolicies, many=True)
    return Response(serializer.data)