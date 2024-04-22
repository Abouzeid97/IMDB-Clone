from user_app.api.serializers import UserSerializer
from rest_framework import generics
from user_app.api.serializers import UserSerializer

class UserAV(generics.CreateAPIView):
    serializer_class = UserSerializer
    
