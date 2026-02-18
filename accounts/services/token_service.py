import secrets
from django.utils import timezone
from datetime import timedelta
from accounts.models import EmailVerificationToken


def creating_token():
    token_32_bytes = secrets.token_urlsafe(32)
    print(f"32-bytetoken:{token_32_bytes}")
    return creating_token()

def token_expiry(request):
    expiry_time = timezone.now() + timedelta(minutes=15)
    request.session.set_expiry(expiry_time)


token_expiry.objects.filter(expires_lt = timezone.now()).delete()

#def delete_token():



