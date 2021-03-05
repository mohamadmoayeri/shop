from django.shortcuts import render

from profiles.models import User

from .serializers import register_serial,login_serial

from rest_framework import status,viewsets,response,permissions,views,generics

#from rest_framework.decorators import api_view

#from rest_framework.generics import ListAPIView,CreateAPIView

#from rest_framework.authentication import TokenAuthentication,SessionAuthentication

#from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny


#from rest_framework_simplejwt.tokens import Refresh


class register(generics.CreateAPIView):

    permission_classes=[permissions.AllowAny,]

    queryset = User.objects.all()

    serializer_class = register_serial

    http_method_names=['post',]
    
    def get_serializer_context(self,**kwargs):

        context=super().get_serializer_context(**kwargs)

        context['p2']=self.request.data['password2']

        return context

        
    



    




    




