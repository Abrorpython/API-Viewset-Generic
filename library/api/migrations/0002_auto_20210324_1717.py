# Generated by Django 3.1.7 on 2021-03-24 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rentbook',
            old_name='returnddate',
            new_name='returndDate',
        ),
    ]
