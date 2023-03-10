# app/accounts/urls.py

# Django modules
from django.urls import path

# Locals
from app.accounts import views 

app_name = 'accounts'

urlpatterns = [
	path('register-user/', views.register_user, name='register_user'),    
	path('register-vendor/', views.register_vendor, name='register_vendor'),    
] 
