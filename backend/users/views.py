"""Views for users app — register, login, profile."""
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    RegisterSerializer, UserProfileSerializer, UserSerializer
)


class RegisterView(generics.CreateAPIView):
    """POST /api/auth/register/ — create new user, return JWT tokens."""
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
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
