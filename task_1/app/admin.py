from django.contrib import admin
from app.models import *

class AdminUserModel(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'password', 'email',)

admin.site.register(UserModel, AdminUserModel)

class AdminUserDetails(admin.ModelAdmin):
    list_display = ('id', 'address', 'phone_number', 'postal_code', 'date_of_birth', 'gender')

admin.site.register(UserDetails, AdminUserDetails)