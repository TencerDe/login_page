from django.urls import path
from .views import SignupView, VerifyEmailView
from .views import LoginView, LogoutView
from .views import ProtectedView
from accounts.views import RefreshTokenView

urlpatterns = [
    path("signup/", SignupView.as_view()),
    path("verify-email/", VerifyEmailView.as_view()),

    path("login/", LoginView.as_view()),
    path("refresh/", RefreshTokenView.as_view()),
    path("logout/", LogoutView.as_view()),

    path("protected/", ProtectedView.as_view()),
]