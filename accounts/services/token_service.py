import secrets
from django.utils import timezone
from datetime import timedelta
from accounts.models import EmailVerificationToken


def create_verification_token(user):
    EmailVerificationToken.objects.filter(
        user=user, is_used = False).delete()
    token=  secrets.token_urlsafe(32)
    expiry_time = timezone.now() + timedelta(minutes=15)
    EmailVerificationToken.objects.create(
        user = user, token = token, expires_at = expiry_time)
    return token


def validate_verification_token(token):
    token_obj = EmailVerificationToken.objects.filter(
        token = token, is_used = False).first()
    if not token_obj:
        return None
    if token_obj.expires_at < timezone.now():
        return None
    return token_obj


def mark_token_used(token_obj):
    token_obj.is_used = True
    token_obj.save()


