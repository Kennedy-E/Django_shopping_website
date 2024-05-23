from django.urls import path, include
app_name = "Delivery"
from .views import *
urlpatterns = [
    path("home/", home, name="home"),
    path("about_us", about_us, name="about_us")
]