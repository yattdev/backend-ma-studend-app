# Generated by Django 3.2.10 on 2022-02-01 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllowedNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10, unique=True, verbose_name="Whats'app")),
            ],
        ),
        migrations.CreateModel(
            name='Communaute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name="Nom de l'association")),
                ('allowed_numbers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.allowednumber', verbose_name="Whats'app des membres d'une communauté")),
            ],
        ),
    ]