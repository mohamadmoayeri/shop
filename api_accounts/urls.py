from django.urls import path

from .views import register,login,logout


urlpatterns = [
    path('register',register.as_view(),name='api_register'),

    path('login',login.as_view(),name='api_login'),

    path('logout',logout.as_view(),name='api_logout'),
    
  

]
