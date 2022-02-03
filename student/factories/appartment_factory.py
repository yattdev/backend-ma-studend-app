#!/usr/bin/env python
# -*- coding: utf-8 -*-

import factory
from faker import Faker
from student.models.appartment import Appartment

# Create object faker
faker = Faker()


class AppartementFactory(factory.django.DjangoModelFactory):
    """ Factory class for student Appartment models """
    class Meta:
        """ Class Meta for AppartementFactory """
        model = Appartment
        # Solution for unique contraint field
        django_get_or_create = ('lessor_name', 'lessor_number')

    description = faker.text()
    site = faker.address()
    is_rented = faker.boolean()
    lessor_name = factory.LazyFunction(lambda x: faker.unique.name())
    lessor_number = factory.LazyFunction(lambda x: faker.unique.msisdn())
    image = factory.django.ImageField(width=350,
                                      height=280,
                                      filename=factory.LazyFunction(
                                          faker.unique.name))
