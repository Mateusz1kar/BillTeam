# Generated by Django 3.0.4 on 2020-03-26 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20200326_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='date_end',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='date_start',
        ),
    ]
