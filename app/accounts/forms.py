# app/accounts/forms.py

# Django modules
from django import forms

# Local
from app.accounts.models import User

class UserRegistrationForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			'first_name', 'last_name', 
			'username', 'email', 'phone_number', 'password'
		]