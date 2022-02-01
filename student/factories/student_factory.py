#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from faker import Faker
import factory
from student.models.student import Student
from users.factories import UserFactory

faker = Faker()


class StudentFactory(factory.django.DjangoModelFactory):
    """ Student profile factory """
    class Meta:
        """ Class Meta """
        model = Student
        django_get_or_create = ("user", )

    user = factory.SubFactory(UserFactory)
    profile_image = factory.django.ImageField(width=400,
                                              height=200,
                                              filename='photo_de_profile.jpg')
