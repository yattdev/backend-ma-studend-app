# Generated by Django 3.2.10 on 2022-01-10 18:41

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_appartment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appartment',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['top', 'left'], default='appartement-default.jpg', force_format=None, keep_meta=True, quality=75, size=[350, 280], upload_to='appartements_images'),
        ),
    ]
