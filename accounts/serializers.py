from rest_framework import serializers
from .models import CustomUser, CustomUserManager, EmailVerificationToken, UserSession, PasswordResetToken

class UserSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id',
                  'user',
                  'refresh_token',
                  'device_name',
                  'ip_address',
                  'created_at',
                  'expires_at',
                  'is_revoked']
        
        read_only_fields = ['ip_address',
                            'created_at',
                            'expires_at']


#THIS SERIALIZER WILL HANDLE PASSWORD HASHING
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, min_lenght = 6)
    class Meta:
        model = CustomUser
        fields = ['email',
                  'password']
        def create(self, validated_data):
            password = validated_data.pop("password")
            user = CustomUser.objects.create_user(password=password , **validated_data)
            return user
        
#THIS SERIALIZER WILL VERIFY EMAILVERIFICATIOPNTOKENS
class EmailVerificationTokenSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 
                  'user',
                  'created_at',
                  'expires_at',
                  'is_used']
        read_only_fields = ['created_at',
                  'is_used']


class UserSessionSerialzer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 
                  'user',
                  'refresh_token',
                  'device_name',
                  'ip_address',
                  'created_at',
                  'expires_at',
                  'is_revoked']
        read_only_fields = ['created_at',
                  'is_revoked']
        
class PasswordResetTokenSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 
                  'user',
                  'created_at',
                  'expires_at',
                  'ip_address',
                  'is_used']
        read_only_fields = ['created_at',
                  'is_used']

