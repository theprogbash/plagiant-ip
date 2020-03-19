from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import University, OriginalDocument

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'website')

class OriginalDocumentAdmin(admin.ModelAdmin):
    list_display = ('document_title', 'student_name', 'teacher_name', 'university', 'date_added', 'document_type')

admin.site.site_header = "plagiant.az - Admin Dashboard" 
admin.site.register(University, UniversityAdmin)
admin.site.register(OriginalDocument, OriginalDocumentAdmin)
admin.site.unregister(Group)