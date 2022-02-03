#!/usr/bin/env python
# -*- coding: utf-8 -*-

import factory
from faker import Faker
from django.contrib.auth import get_user_model
from student import signals
from student.factories.utils_models_factory import CommunityFactory

# Create object faker
fake = Faker()

# Get Custom user as User models
User = get_user_model()


# Mute profile create signals
@factory.django.mute_signals(signals.post_save)
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        # Solution for unique contraint field
        django_get_or_create = ('email', 'username')

    first_name = factory.LazyAttribute(lambda x: fake.first_name())
    last_name = factory.LazyAttribute(lambda x: fake.last_name())
    username = factory.LazyAttribute(lambda x: fake.name())
    password = factory.LazyAttribute(lambda x: fake.password())
    email = factory.LazyAttribute(lambda x: fake.email())
    phone = factory.LazyAttribute(lambda x: fake.msisdn())
    communaute = factory.SubFactory(CommunityFactory)
    is_superuser = False


# Another, different, factory for the same object
class AdminFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        # Solution for unique contraint field
        django_get_or_create = ('email', 'username')

    first_name = factory.LazyAttribute(lambda x: fake.first_name())
    last_name = factory.LazyAttribute(lambda x: fake.last_name())
    username = factory.LazyAttribute(lambda x: fake.name())
    password = factory.LazyAttribute(lambda x: fake.password())
    email = factory.LazyAttribute(lambda x: fake.email())
    phone = factory.LazyAttribute(lambda x: fake.msisdn())
    communaute = factory.SubFactory(CommunityFactory)
    is_superuser = True
