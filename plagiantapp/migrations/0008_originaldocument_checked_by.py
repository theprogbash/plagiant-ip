# Generated by Django 2.2.10 on 2020-03-19 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plagiantapp', '0007_auto_20200319_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='originaldocument',
            name='checked_by',
            field=models.ForeignKey(default=13, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
