# Generated by Django 3.0.4 on 2020-03-25 21:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0005_auto_20200325_2229'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Person2',
        ),
    ]
