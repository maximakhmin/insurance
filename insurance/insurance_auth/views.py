from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import User
from django.db.utils import IntegrityError
from rest_framework.decorators import api_view, permission_classes
from insurance_auth.permissions import IsAuthenticated

# Create your views here.


@api_view(('POST',)) 
def login(request): 
    data = {
        'email': request.data.get("email"),
        'password': request.data.get("password")
    }

    user = authenticate(username=data['email'],
                        password=data['password'])
    
    if (user):
        return Response(user.token)
    else:
        return Response("Cannot login, check your email and password.")
    
@api_view(('POST',))
def register(request):
    data = {
        'email': request.data.get("email"),
        'password': request.data.get("password")
    }
    try:
        if User.objects.create_user(data['email'], data['password']):
            return Response(f'User created. Email:{data["email"]}/ Password:{data["password"]}')
        else:
            return Response('Enter email')
    except IntegrityError:
        return Response('This email is already taken')
    


@api_view(('GET',))
@permission_classes([IsAuthenticated])
def who(request):

    if (request.user):
        return Response(request.user.email)
    else:
        return Response("Error with authorization")
    
