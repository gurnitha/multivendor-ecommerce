# app/accounts/views.py

# Django modules
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register_user(request):
	return render(request, 'app/accounts/register-user.html')
