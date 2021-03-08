from django.shortcuts import render

from profiles.models import User

from .serializers import register_serial,login_serial,logout_serial

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

        
class login(generics.GenericAPIView):

    serializer_class = login_serial

    permission_classes=[permissions.AllowAny,]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class logout(generics.GenericAPIView):
    serializer_class = logout_serial

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(status=status.HTTP_204_NO_CONTENT)
    




    




