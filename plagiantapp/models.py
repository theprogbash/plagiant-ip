from django.db import models

class University(models.Model):
    name = models.TextField(max_length=150)
    logo = models.ImageField(upload_to='static/images/university_logo')
    website = models.URLField()

    class Meta:
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.name
