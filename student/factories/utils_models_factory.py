#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from faker import Faker
import factory
from student.models.utils_models import Community, AllowedNumber

faker = Faker()


class CommunityFactory(factory.django.DjangoModelFactory):
    """ Class Factory for Community models from student app """
    class Meta:
        """ Class Meta in CommunityFactory """
        model = Community
        django_get_or_create = ("name", )

    name = factory.LazyAttribute(lambda x: faker.company())


class AllowedNumberFactory(factory.django.DjangoModelFactory):
    """ Class Factory for AllowedNumber models from student app """
    class Meta:
        """ Class Meta inside AllowedNumberFactory """
        model = AllowedNumber
        django_get_or_create = ("phone", )

    phone = factory.LazyAttribute(lambda x: faker.msisdn())
    community = factory.SubFactory(CommunityFactory)
