from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from backend.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Simple User ViewSet
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
