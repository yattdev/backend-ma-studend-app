# Generated by Django 3.2.10 on 2022-02-03 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_useraccount_communaute'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='communaute',
            new_name='community',
        ),
    ]