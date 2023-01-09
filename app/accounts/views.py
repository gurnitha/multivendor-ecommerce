# app/accounts/views.py

# Django modules
from django.shortcuts import render
from django.shortcuts import redirect

# Locals
from app.accounts.forms import UserRegistrationForm
from app.accounts.models import User

# Create your views here.


def register_user(request):
	# Check if the request is POST or GET
	
	# if the request is post
	if request.method == 'POST':
		print(request.POST)
		form = UserRegistrationForm(request.POST)

		# Check if the form is valid
		if form.is_valid():
			''' If form is valid, the submited 
			data is ready to be save,
			but do not save it yet.
			Assign the data to the user '''
			user = form.save(commit=False)
			# Add role to the user
			user.role = User.CUSTOMER
			user.save()
			return redirect('accounts:register_user')

	# if the request is GET
	else:
		form = UserRegistrationForm
	
	context = {
		'form': form,
	}
	return render(request, 'app/accounts/register-user.html', context)
