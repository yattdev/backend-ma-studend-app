#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from student.models.student import Student
from django.dispatch import receiver
from django.db.models.signals import post_save

# Get active user from database
User = get_user_model()


# Create student profile, while create user signal is triggle
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)


# Save profile when user save signal triggle
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.student.save()
