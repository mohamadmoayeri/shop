from django.shortcuts import render

# Create your views here.
from profiles.models import ads

from rest_framework import viewsets,permissions,authentication

from .serializers import home_serial


class home(viewsets.ModelViewSet):
    
    queryset=ads.objects.select_related('user').all()

    serializer_class=home_serial

    permission_classes=[permissions.IsAuthenticated,]

    http_method_names=['get',]

    