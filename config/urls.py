# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path

# Locals
from config import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
