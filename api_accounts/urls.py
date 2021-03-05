from django.urls import path

from .views import register


urlpatterns = [
    path('register',register.as_view(),name='api_register'),
    
  

]
