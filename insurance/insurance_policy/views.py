from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Policy
from .serializer import PolicySerializer
# Create your views here.


class PolicyView(APIView):

    def get(self, request):
        policies = Policy.objects
        serializer = PolicySerializer(policies, many=True)
        return Response(serializer.data)
    

    
    def post(self, request):
        data = {
            'type': request.data.get('type'),
            'cost': request.data.get('cost'),
            'payment': request.data.get('payment'),
            'description': request.data.get('description'),
        }
        serializer = PolicySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response('Saved policy')
        else:
            print("Error with saving data")
            return Response('Error')
        


class PolicyViewOne(APIView):

    http_method_names = ['delete', 'get', 'put']

    def get(self, request, id):
        try:
            policy = Policy.objects.get(id=id)
            serializer = PolicySerializer(policy)
            return Response(serializer.data)
        except Policy.DoesNotExist:
            return Response("No such id")
        except Exception as e:
            print(e)
            return Response("Error")
        
    def delete(self, request, id):
        try:
            Policy.objects.get(id=id).delete()
            return Response("Deleted")
        except Policy.DoesNotExist:
            return Response("No such id")
        except Exception as e:
            print(e)
            return Response("Error")
        
    def put(self, request, id):
        try:
            policy = Policy.objects.get(id=id)
            data = {
                'type': request.data.get('type'),
                'cost': request.data.get('cost'),
                'payment': request.data.get('payment'),
                'description': request.data.get('description'),
            }
            policy.type = data["type"]
            policy.cost = data["cost"]
            policy.payment = data["payment"]
            policy.description = data["description"]

            policy.save()
            return Response("Updated")
        except Policy.DoesNotExist:
            return Response("No such id")
        except Exception as e:
            print(e)
            return Response("Error")

        
    
@api_view(('GET',)) 
def activatePolicy(request, id):
    try:
        policy = Policy.objects.get(id=id)
        policy.active = True
        policy.save()
        return Response("Policy activated")
    except Policy.DoesNotExist:
        return Response("No such id")
    except Exception as e:
        print(e)
        return Response("Error")
    
@api_view(('GET',)) 
def deactivatePolicy(request, id):
    try:
        policy = Policy.objects.get(id=id)
        policy.active = False
        policy.save()
        return Response("Policy deactivated")
    except Policy.DoesNotExist:
        return Response("No such id")
    except Exception as e:
        print(e)
        return Response("Error")