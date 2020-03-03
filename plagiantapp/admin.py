from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import University, Account

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'website')

class AccountAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'username', 'password', 'isPhysicalAccount', 'university_name')

admin.site.site_header = "plagiant.az - Admin Dashboard" 
admin.site.register(University, UniversityAdmin)
admin.site.register(Account, AccountAdmin)
# admin.site.unregister(User)
admin.site.unregister(Group)