from django.urls import path,include

from rest_framework.routers import DefaultRouter

from .views import home

router=DefaultRouter()

router.register('api_home',home,basename='api_home')




urlpatterns = [
    
]

urlpatterns += router.urls