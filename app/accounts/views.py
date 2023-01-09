# app/accounts/views.py

# Django modules
from django.shortcuts import render

# Locals
from app.accounts.forms import UserRegistrationForm

# Create your views here.


def register_user(request):
	form = UserRegistrationForm
	context = {
		'form':form,
	}
	return render(request, 'app/accounts/register-user.html', context)
