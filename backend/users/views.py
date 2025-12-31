# from rest_framework import generics
# from .serializers import RegisterSerializer
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User
from .serializer import RegisterSerializer
from .encryption import decrypt_data


# 🔹 Phase 1: Registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


# 🔹 Phase 3: Secure Profile Fetch
class ProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "email": user.email,
            "aadhaar": decrypt_data(user.aadhaar_encrypted)
        })
