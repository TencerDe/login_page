from rest_framework import serializers
from .models import CustomUser, EmailVerificationToken, UserSession, PasswordResetToken
from django.utils import timesince, timezone

class UserSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSession
        fields = ['id',
                  'device_name',
                  'ip_address',
                  'created_at',
                  'expires_at',
                  'is_revoked']
        
        read_only_fields = ["ip_address", "created_at", "expires_at", "is_revoked"]


#THIS SERIALIZER WILL HANDLE PASSWORD HASHING
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, min_length = 6)
    class Meta:
        model = CustomUser
        fields = ['email',
                  'password']
        
    def validate_email(self, value):
        value = value.strip().lower()
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already re gistered")
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser.objects.create_user(password=password , **validated_data)
        return user
        
#THIS SERIALIZER WILL VERIFY EMAILVERIFICATIOPNTOKENS
class EmailVerificationTokenSerializer(serializers.Serializer):
    
    token = serializers.CharField()

    def validate_token(self, value):
        try:
            token_obj = EmailVerificationToken.objects.get(Token=value, is_used = False)
        except EmailVerificationToken.DoesNotExist:
            raise serializers.ValidationError('Invalid or expired verification tokens')
        if token_obj.expires_at < timezone.now():
            raise serializers.ValidationError("Verification link has expired")

        return value

        
class PasswordResetTokenSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField(write_only = True, min_length = 6)