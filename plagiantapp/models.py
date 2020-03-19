from django.db import models
from django.contrib.auth.models import User
from django_currentuser.db.models import CurrentUserField

class University(models.Model):
    name = models.TextField(max_length=150)
    logo = models.ImageField(upload_to='static/images/university_logo')
    website = models.URLField()

    class Meta:
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.name

class OriginalDocument(models.Model):
    document = models.FileField(upload_to='static/original_document', blank=False)
    document_title = models.CharField(max_length=300)
    student_name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    document_type = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add = True)
    checked_by = CurrentUserField()

    def __str__(self):
        return self.document_title

