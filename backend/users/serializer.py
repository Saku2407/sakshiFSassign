# from rest_framework import serializers
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ['email', 'password']

#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)


from rest_framework import serializers
from .models import User
from .encryption import encrypt_data


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class ProfileSerializer(serializers.ModelSerializer):
    aadhaar = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'aadhaar']

    def update(self, instance, validated_data):
        instance.aadhaar_encrypted = encrypt_data(validated_data['aadhaar'])
        instance.save()
        return instance
