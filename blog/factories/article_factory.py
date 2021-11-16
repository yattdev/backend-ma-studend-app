#!/usr/bin/env python
# -*- coding: utf-8 -*-

import factory
import random
from faker import Faker
from blog.models.article_models import Article
from .category_factory import CategoryFactory
from users.factories import UserFactory
from django.core.files.base import ContentFile

# Creat object faker
fake = Faker()


class ArticleFactory(factory.django.DjangoModelFactory):
    """Factory models for blog:article models """
    class Meta:
        model = Article
        # Solution for unique contraint field
        django_get_or_create = ('author', 'title')

    category = factory.SubFactory(CategoryFactory)
    title = fake.name()
    author = factory.SubFactory(UserFactory)
    image = factory.LazyAttribute(
            lambda _: ContentFile(
                factory.django.ImageField()._make_data(
                    {'width': 1024, 'height': 768}
                ), 'example.jpg'
            )
        )
    image_credit = fake.name()
    body = fake.paragraph(nb_sentences=100)
    tags = fake.name()
    status = 'Publish'
    read_time = random.randrange(6)

