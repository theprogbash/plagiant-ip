from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import University

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'website')

admin.site.site_header = "plagiant.az - Admin Dashboard" 
admin.site.register(University, UniversityAdmin)
admin.site.unregister(Group)