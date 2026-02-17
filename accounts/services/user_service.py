from django.contrib.auth.base_user import BaseUserManager
from accounts.models import CustomUser

def create_user_for_signup(email, password, **extra_fields):
    extra_fields.setdefault("is_verified", False)

    user = CustomUser.objects.create_user(
        email=email,
        password=password,
        **extra_fields
    )

    return user
