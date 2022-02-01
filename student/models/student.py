#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField

# Get active user model
User = get_user_model()


class Student(models.Model):
    """ Student Profile """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = ResizedImageField(verbose_name="Image du profile",
                                      default='profile-pic-default.jpg',
                                      upload_to='profile_pic',
                                      crop=["top", "left"],
                                      size=[200, 200])
