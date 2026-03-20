from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer, LoginSerializer

from accounts.services.user_service import create_user_for_signup
from accounts.services.token_service import (create_verification_token,
    validate_verification_token,
    mark_token_used
)
from accounts.services.email_service import send_verification_email
from accounts.services.auth_service import authenticate_user
from accounts.services.jwt_service import generate_tokens_for_user
from accounts.services.session_service import create_user_session
from accounts.services.session_service import revoke_session


from accounts.models import UserSession



# Create your views here.


class SignupView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]


        user = create_user_for_signup(email=email, password=password)
        token = create_verification_token(user)
        send_verification_email(user, token)

        return Response(
            {
                "message": "Signup successful. Please verify your email."
            },
            status=status.HTTP_201_CREATED
        )


class VerifyEmailView(APIView):

    def get(self, request):
        token = request.query_params.get("token")

        if not token:
            return Response(
                {"error": "Token is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        token_obj = validate_verification_token(token)

        if not token_obj:
            return Response(
                {"error": "Invalid or expired token."},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = token_obj.user

        # mark token used
        mark_token_used(token_obj)

        # verify user
        user.is_verified = True
        user.save()

        return Response(
            {"message": "Email verified successfully."},
            status=status.HTTP_200_OK
        )



class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate_user(email, password)

        tokens = generate_tokens_for_user(user)

        create_user_session(
            user=user,
            refresh_token=tokens["refresh_token"],
            request=request
        )

        return Response(
            {
                "access_token": tokens["access_token"],
                "refresh_token": tokens["refresh_token"],
                "message": "Login successful"
            },
            status=status.HTTP_200_OK
        )
    

class RefreshTokenView(APIView):

    def post(self, request):
        refresh_token = request.data.get("refresh_token")

        if not refresh_token:
            return Response(
                {"error": "Refresh token required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        session = UserSession.objects.filter(
            refresh_token=refresh_token,
            is_revoked=False
        ).first()

        if not session:
            raise AuthenticationFailed("Invalid session")

        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
        except Exception:
            raise AuthenticationFailed("Invalid token")

        return Response(
            {"access_token": access_token},
            status=status.HTTP_200_OK
        )


class LogoutView(APIView):

    def post(self, request):
        refresh_token = request.data.get("refresh_token")

        if not refresh_token:
            return Response(
                {"error": "Refresh token required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        revoke_session(refresh_token)

        return Response(
            {"message": "Logged out successfully"},
            status=status.HTTP_200_OK
        )
    
    def blacklist_token(refresh_token):
    token = RefreshToken(refresh_token)
    token.blacklist()


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello {request.user.email}"})


permission_classes = [IsAuthenticated, IsVerifiedUser]


class SecureView(APIView):
    permission_classes = [IsAuthenticated, IsVerifiedUser]

    def get(self, request):
        return Response({"message": "Secure data"})


