from django.urls import path

from .views import upload_ads,edit_ads,delete_account 

urlpatterns = [
    path("delete_account",delete_account,name="delete_account"),

    path("upload-ads/<str:user>",upload_ads.as_view(),name="upload-ads"),
    
    path("edit-ads/<int:pk>",edit_ads.as_view(),name="edit_ads"),



]