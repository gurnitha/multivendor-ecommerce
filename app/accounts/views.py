# app/accounts/views.py

# Django modules
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages, auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.template.defaultfilters import slugify

# Locals
from app.accounts.forms import UserRegistrationForm
from app.accounts.models import User, UserProfile
from app.vendor.forms import VendorRegistrationForm
from app.accounts.utils import detect_user



# Restrict the vendor from accessing the customer page
def check_role_vendor(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied


# Restrict the customer from accessing the vendor page
def check_role_customer(user):
    if user.role == 2:
        return True
    else:
        raise PermissionDenied


# User: register
def register_user(request):

	# Handling the loggeg in user
	if request.user.is_authenticated:
		messages.warning(request, 'You are already logged in!')
		return redirect('accounts:dashboard')

	# Check if the request is POST or GET
	
	# if the request is post
	if request.method == 'POST':
		print(request.POST)
		ureg_form = UserRegistrationForm(request.POST)

		# CREATE USER USING THE FORM

		# # Check if the ureg_form is valid
		# if ureg_form.is_valid():
		# 	# Clean the data
		# 	password = ureg_form.cleaned_data['password']
		# 	''' If ureg_form is valid, the submited 
		# 	data is ready to be save,
		# 	but do not save it yet.
		# 	Assign the data to the user '''
		# 	user = ureg_form.save(commit=False)
		# 	# Store passward in hash format
		# 	user.set_password(password)
		# 	# Add role to the user
		# 	user.role = User.CUSTOMER
		# 	user.save()
		# 	return redirect(register_user)

		# CREATE USER USING create_user METHOD
		
		if ureg_form.is_valid():
			'''Get the first_name, last_name, username,
			email, password form the create_user method
			and assign the role as CUSTOMER'''
			first_name = ureg_form.cleaned_data['first_name']
			last_name = ureg_form.cleaned_data['last_name']
			username = ureg_form.cleaned_data['username']
			email = ureg_form.cleaned_data['email']
			password = ureg_form.cleaned_data['password']
			user = User.objects.create_user(
				first_name=first_name, 
				last_name=last_name, 
				username=username, 
				email=email, 
				password=password)
			user.role = User.CUSTOMER
			user.save()
			messages.success(request, 'Your account has been registered sucessfully!')
			# print('User is created')
			return redirect('accounts:register_user')

		else:
			print('invalid ureg_form')
			print(ureg_form.errors)


	# if the request is GET
	else:
		ureg_form = UserRegistrationForm()
	
	context = {
		'ureg_form': ureg_form,
	}
	
	# return render(request, 'accounts/register-user.html', context)
	return render(request, 'app/accounts/register-user.html', context)


# Vendor: register
def register_vendor(request):

	# Handling the loggeg in user
	if request.user.is_authenticated:
		messages.warning(request, 'You are already logged in!')
		return redirect('accounts:dashboard')

	# Check if the request is POST
	elif request.method == 'POST':
		# Store the data and create user
		ureg_form = UserRegistrationForm(request.POST)
		vreg_form = VendorRegistrationForm(request.POST, request.FILES)
		# Check if form is valid
		if ureg_form.is_valid() and vreg_form.is_valid():
			first_name = ureg_form.cleaned_data['first_name']
			last_name = ureg_form.cleaned_data['last_name']
			username = ureg_form.cleaned_data['username']
			email = ureg_form.cleaned_data['email']
			password = ureg_form.cleaned_data['password']
			user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
			user.role = User.VENDOR
			user.save()
			# Do not save this user to vreg_form
			vendor = vreg_form.save(commit=False)
			vendor.user = user 
			# Get user profile from User which defined in signals

			vendor_name = vreg_form.cleaned_data['vendor_name']
			vendor.vendor_slug = slugify(vendor_name)+'-'+str(user.id)
			user_profile = UserProfile.objects.get(user=user)
			vendor.user_profile = user_profile
			vendor.save()
			messages.success(request, 'Your account has been registered sucessfully! Please wait for the approval.')
			return redirect('accounts:register_vendor')
		else:
			print('invalid ureg_form and vreg_form')
			print(ureg_form.errors)
			print(vreg_form.errors)
	else:
		ureg_form = UserRegistrationForm()
		vreg_form = VendorRegistrationForm()

	context = {
		'ureg_form': ureg_form,
		'vreg_form': vreg_form
	}
	return render(request, 'app/accounts/register-vendor.html', context)


# User or Vendor: Login
def login(request):
	# Handling the loggeg in user
	if request.user.is_authenticated:
		messages.warning(request, 'You are already logged in!')
		return redirect('accounts:my_account')

	elif request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = auth.authenticate(email=email, password=password)
		# If user exist
		if user is not None:
			auth.login(request, user)
			messages.success(request, 'You are now logged in.')
			return redirect('accounts:my_account')
		# If user is not exist
		else: 
			messages.error(request, 'Invalid login credentials')
			return redirect('accounts:login')
	return render(request, 'app/accounts/login.html')


# Logout: Customer or Vendor
def logout(request):
	auth.logout(request)
	messages.info(request, 'You are logged out. Login again?')
	return redirect('accounts:login')


def my_account(request):
    user = request.user
    redirectUrl = detect_user(user)
    return redirect(redirectUrl)


@login_required(login_url='accounts:login')
@user_passes_test(check_role_customer)
def customer_dashboard(request):
    return render(request, 'app/accounts/customer-dashboard.html')


@login_required(login_url='accounts:login')
@user_passes_test(check_role_vendor)
def vendor_dashboard(request):
    return render(request, 'app/accounts/vendor-dashboard.html')

# Dashboard
def dashboard(request):
	return render(request, 'app/accounts/dashboard.html')