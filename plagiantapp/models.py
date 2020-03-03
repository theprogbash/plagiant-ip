from django.db import models

class University(models.Model):
    name = models.TextField(max_length=150)
    logo = models.ImageField(upload_to='static/images/university_logo')
    website = models.URLField()
    class Meta:
        verbose_name_plural = "Universities"
    def __str__(self):
        return self.name

class Account(models.Model):
    first_name = models.TextField(max_length=30)
    last_name = models.TextField(max_length=30)
    email = models.EmailField(max_length=60)
    username = models.TextField(max_length=30)
    password = models.TextField(max_length=60)
    confirm_password = models.TextField(max_length=60)
    isPhysicalAccount = models.BooleanField(default=False)
    university_name = models.ForeignKey(University, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username
