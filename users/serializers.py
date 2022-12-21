from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_superuser']
        extra_kwargs= {'password':{'write_only': True},
        'email': {'validators':[UniqueValidator(queryset=User.objects.all())],'required': True },
        'username': {'validators':[UniqueValidator(queryset=User.objects.all(), message="A user with that username already exists.")],'required': True }}
        read_only_fields = ['id']

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
    
    
