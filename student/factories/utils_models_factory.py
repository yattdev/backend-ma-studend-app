#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from faker import Faker
import factory
from student.models.utils_models import Communaute, AllowedNumber

faker = Faker()


class CommunauteFactory(factory.django.DjangoModelFactory):
    """ Class Factory for Communaute models from student app """
    class Meta:
        """ Class Meta in CommunauteFactory """
        model = Communaute
        django_get_or_create = ("name", )

    name = factory.LazyAttribute(lambda: faker.company())


class AllowedNumberFactory(factory.django.DjangoModelFactory):
    """ Class Factory for AllowedNumber models from student app """
    class Meta:
        """ Class Meta inside AllowedNumberFactory """
        model = AllowedNumber
        django_get_or_create = ("phone", )

    phone = factory.LazyAttribute(lambda: fake.msisdn())
    communaute = factory.SubFactory(CommunauteFactory)
