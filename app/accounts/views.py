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

		# CREATE USER USING THE FORM

		# # Check if the form is valid
		# if form.is_valid():
		# 	# Clean the data
		# 	password = form.cleaned_data['password']
		# 	''' If form is valid, the submited 
		# 	data is ready to be save,
		# 	but do not save it yet.
		# 	Assign the data to the user '''
		# 	user = form.save(commit=False)
		# 	# Store passward in hash format
		# 	user.set_password(password)
		# 	# Add role to the user
		# 	user.role = User.CUSTOMER
		# 	user.save()
		# 	return redirect('accounts:register_user')

		# CREATE USER USING create_user METHOD

		if form.is_valid():
			'''Get the first_name, last_name, username,
			email, password form the create_user method
			and assign the role as CUSTOMER'''
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user = User.objects.create_user(
				first_name=first_name, last_name=last_name, 
				username=username, email=email, password=password)
			user.role = User.CUSTOMER
			user.save()
			print('User is created!')
			return redirect('accounts:register_user')
			
	# if the request is GET
	else:
		form = UserRegistrationForm
	
	context = {
		'form': form,
	}
	return render(request, 'app/accounts/register-user.html', context)
