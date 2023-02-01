from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

users = []

@api_view(['GET'])
def endpoints(request):
    data = ['/', '/api/v1/users']
    return Response(data)

@api_view(['POST'])
def user_create(request):
    data = request.data

    user = {
        'username': data['username']
    }

    users.append(user)

    return Response(users)

@api_view(['GET'])
def user_list(request):
    return Response(users)

@api_view(['GET'])
def user_get(request, username):
    
    for user in users:
        if user['username'] == username:
            return Response(user)

    return Response('User not found.')