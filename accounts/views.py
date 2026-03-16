from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterSerializer

from accounts.services.user_service import create_user_for_signup
from accounts.services.token_service import create_verification_token
from accounts.services.email_service import send_verification_email


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

