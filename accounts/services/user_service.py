from django.contrib.auth.base_user import BaseUserManager


class signup():
    def create_user_for_signup(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Please enter a email address')
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        user.is_verified = False
        return user



