from django.urls import path

from .views import dashboard,Edit_Profile,change_password,change_password_done,delete_avatar,delete_ads

urlpatterns = [
    path("dashboard",dashboard.as_view(),name="dashboard"),

    path("Edit_Profile/<int:pk>",Edit_Profile.as_view(),name="Edit_Profile"),

    path("change_password",change_password.as_view(),name="change_password"),

    path("change_password_done20212",change_password_done.as_view(),name="change_password_done"),

    path("delete_avatar/<int:pk>",delete_avatar,name="delete_avatar"),

    path("delete_ads/<int:pk>",delete_ads,name="delete_ads"),


    






]