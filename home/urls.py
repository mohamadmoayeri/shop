from django.urls import path

from .views import home,categories

urlpatterns = [
    path("",home.as_view(),name="home"),

    path("categories/<slug:category>",categories.as_view(),name="category"),
]