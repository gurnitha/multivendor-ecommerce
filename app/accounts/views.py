# app/accounts/views.py

# Django modules
from django.shortcuts import render

# Locals
from app.accounts.forms import UserRegistrationForm

# Create your views here.


def register_user(request):
	# Check if the request is POST or GET
	
	# if the request is post
	if request.method == 'POST':
		print(request.POST)

	# if the request is GET
	else:
		form = UserRegistrationForm
	
	context = {
		'form': form,
	}
	
	return render(request, 'app/accounts/register-user.html', context)
