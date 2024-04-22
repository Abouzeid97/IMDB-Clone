from rest_framework import serializers
from watchlist_app.models import User

class UserSerializer(serializers.ModelSerializer):
    
    password_confirmation = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation')

        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            },
        }

    # def validate(self, data):

    #     if data['password']!= data['password_confirmation']:
    #         raise serializers.ValidationError('Passwords do not match.')
    #     elif User.objects.filter(email=data['email']).exists():
    #         raise serializers.ValidationError('email is already exists')
    #     else:
    #         return data
    def save(self):
        password = self.validated_data['password']
        password_confirmation = self.validated_data['password_confirmation']

        if password != password_confirmation:
            raise serializers.ValidationError('Passwords do not match.')
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError('email is already exists')
        
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account

