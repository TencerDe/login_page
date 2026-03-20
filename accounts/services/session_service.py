from django.utils import timezone
from datetime import timedelta
from accounts.models import UserSession


def create_user_session(user, refresh_token, request):
    ip = request.META.get("REMOTE_ADDR")
    device = request.META.get("HTTP_USER_AGENT", "unknown")

    expiry = timezone.now() + timedelta(days=7)

    return UserSession.objects.create(
        user=user,
        refresh_token=refresh_token,
        device_name=device,
        ip_address=ip,
        expires_at=expiry
    )


def revoke_session(refresh_token):
    session = UserSession.objects.filter(
        refresh_token=refresh_token,
        is_revoked=False
    ).first()

    if session:
        session.is_revoked = True
        session.save()