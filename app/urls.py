from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('weather/', weatherview, name='weather'),
    path('weather-app/', weather_page, name='weather-app'),
] 