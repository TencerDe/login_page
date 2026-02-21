from django.core.mail import send_mail
from django.conf import settings


def send_verification_email(user, token):

    verification_link = f"{settings.FRONTEND_URL}/verify-email/?token={token}"

    subject = "Verify your email address"
    message = (
        f"Hi,\n\n"
        f"Please verify your email by clicking the link below:\n\n"
        f"{verification_link}\n\n"
        f"If you did not sign up, please ignore this email."
    )

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )
