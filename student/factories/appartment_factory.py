#!/usr/bin/env python
# -*- coding: utf-8 -*-

import factory
from faker import Faker
from student.models.appartment_models import Appartment

# Create object faker
fake = Faker()


class AppartementFactory(factory.django.DjangoModelFactory):
    """ Factory class for student Appartment models """
    class Meta:
        """ Class Meta for AppartementFactory """
        model = Appartment
        # Solution for unique contraint field
        django_get_or_create = ('lessor_name', 'lessor_number')

    description = fake.text()
    site = fake.address()
    is_rented = fake.boolean()
    lessor_name = factory.LazyFunction(fake.unique.name)
    lessor_number = factory.LazyFunction(fake.unique.msisdn)
    image = factory.django.ImageField(width=350,
                                      height=280,
                                      filename=factory.LazyFunction(
                                          fake.unique.name))
