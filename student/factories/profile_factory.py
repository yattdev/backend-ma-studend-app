#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from faker import Faker
import factory
from student.models.profile_models import Profile
from users.factories import UserFactory

faker = Faker()


class ProfileFactory(factory.django.DjangoModelFactory):
    """ Profile profile factory """
    class Meta:
        """ Class Meta """
        model = Profile
        django_get_or_create = ("user", )

    user = factory.SubFactory(UserFactory)
    profile_image = factory.django.ImageField(width=400,
                                              height=200,
                                              filename='photo_de_profile.jpg')
