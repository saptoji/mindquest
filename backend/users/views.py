"""Views for users app — register, login, profile."""
import traceback
import logging
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    RegisterSerializer, UserProfileSerializer, UserSerializer
)

logger = logging.getLogger(__name__)


class RegisterView(generics.CreateAPIView):
    """POST /api/auth/register/ — create new user, return JWT tokens."""
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Registrasi berhasil!',
                'user': UserSerializer(user).data,
                'tokens': {
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                }
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            tb = traceback.format_exc()
            logger.error(f"Registration error: {e}\n{tb}")
            return Response(
                {"error": str(e), "traceback": tb},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ProfileView(generics.RetrieveAPIView):
    """GET /api/auth/profile/ — return current user's profile + stats."""
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user.profile


class CurrentUserView(generics.RetrieveAPIView):
    """GET /api/auth/me/ — return basic info of authenticated user."""
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
