from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()


def authenticate_user(email, password):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        raise AuthenticationFailed("Invalid credentials.")

    if not check_password(password, user.password):
        raise AuthenticationFailed("Invalid credentials.")

    if not user.is_verified:
        raise AuthenticationFailed("Email not verified.")

    if not user.is_active:
        raise AuthenticationFailed("User is inactive.")

    return user