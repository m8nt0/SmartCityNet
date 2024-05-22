# user_view.py

from rest_framework import viewsets
from django.contrib.auth import get_user_model
from backend.serializers.user_serializer import UserSerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
