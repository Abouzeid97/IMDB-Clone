from user_app.api.serializers import UserSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from user_app import models

@api_view(['POST',])
def logout(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({'Response': 'Logout Successfully'})

@api_view(['POST',])
def RegistrationView(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data = {} 
        if serializer.is_valid():
            account = serializer.save()
            data['Response'] = "Registration Successfully"
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)
# class UserAV(generics.CreateAPIView):
#     serializer_class = UserSerializer
    
