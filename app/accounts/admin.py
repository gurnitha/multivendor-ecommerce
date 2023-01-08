# config/admin.py

# Import django modules
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Import dari locals
from app.accounts.models import User 

# Register your models here.

class UserAdmin(UserAdmin):
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, UserAdmin)
