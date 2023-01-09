# apps/vendors/admin.py

# Django modules
from django.contrib import admin

# Locals
from app.vendor.models import Vendor

# Register your models here.
admin.site.register(Vendor)