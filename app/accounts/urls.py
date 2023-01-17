# app/accounts/urls.py

# Django modules
from django.urls import path

# Locals
from app.accounts import views 

app_name = 'accounts'

urlpatterns = [

	# Register
	path('register-user/', views.register_user, name='register_user'),    
	path('register-vendor/', views.register_vendor, name='register_vendor'),

	# Login, logout, dashboard
	path('login/', views.login, name='login'),    
	path('logout/', views.logout, name='logout'),
	path('dashboard/', views.dashboard, name='dashboard'),
] 
