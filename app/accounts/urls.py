# app/accounts/urls.py

# Django modules
from django.urls import path

# Locals
from app.accounts import views 

app_name = 'accounts'

urlpatterns = [
	path('register-user', views.register_user, name='register_user'),    
] 
