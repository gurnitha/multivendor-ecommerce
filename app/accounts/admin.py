# config/admin.py

# Import django modules
from django.contrib import admin

# Import dari locals
from app.accounts.models import User 

# Register your models here.

admin.site.register(User)