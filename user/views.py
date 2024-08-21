from rest_framework import generics
from user.models import GeneratePassword
from rest_framework.response import Response
from user.serializers import RegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.timezone import now

from datetime import datetime


class RegistrationView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        password = request.data['password']
        generatepasswords = GeneratePassword.objects.filter(password=password)
        if generatepasswords:
            for generatepassword in generatepasswords:
                if (now() - generatepassword.time).total_seconds() < 60:
                    refresh_token = RefreshToken.for_user(generatepassword.user)
                    return Response({
                            'refresh': str(refresh_token),
                            'access': str(refresh_token.access_token)
                        })
                return Response("Parolning faollik muddati 1 daqiqa!")
        return Response("Parol hali yaratilmagan!")