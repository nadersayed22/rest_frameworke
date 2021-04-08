from .models import USerProfile
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """class serialize data from model"""

    class Meta:
        model = USerProfile
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {
                        'password': {'write_only': True, 'style': {'input_type': 'password'}
                                     }}

    def create(self, data):
        """"create ser data of user """
        user = USerProfile(
            email=data['email'],
            name=data['name'],
            password=data['password']
        )
        return user
