# apps/vendors/admin.py

# Django modules
from django.contrib import admin

# Locals
from app.vendor.models import Vendor

# Register your models here.

class VendorAdmin(admin.ModelAdmin):
	list_display = ('user', 'vendor_name', 'is_approved', 'created_at')
	list_display_links = ('user', 'vendor_name')

admin.site.register(Vendor, VendorAdmin)