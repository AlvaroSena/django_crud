from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

# Create your views here.

@api_view(['GET'])
def endpoints(request):
    data = ['/', '/api/v1/users']
    return Response(data)

@api_view(['POST'])
def user_create(request):
    data = request.data

    password_hashed = make_password(data['password'])

    user_exists = User.objects.filter(email=data['email'])

    if user_exists:
        return Response({'Error': 'Email already taken'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        user = User(
            username=data['username'], 
            email=data['email'], 
            password=password_hashed
        )

        user.save()  

        serializer = UserSerializer(user)  

        return Response(serializer.data)
@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def user_get(request, username):
    
    user = User.objects.get(username=username)
    if user:
        serializer = UserSerializer(user)

        return Response(serializer.data)
    else:
        return Response({'Error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)