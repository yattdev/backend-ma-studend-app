#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import shutil

from django.conf import settings
from django.test import TestCase, override_settings
from student.factories.utils_models_factory import (CommunauteFactory,
                                                    AllowedNumberFactory)
from student.models.utils_models import Communaute, AllowedNumber


class CommunauteTestCase(TestCase):
    """ TestCase for models Communaute from student app """
    @classmethod
    def setUpClass(cls):
        # Create a bactch of Communaute
        cls.communautes = CommunauteFactory.create_batch(10)

        # Fetch third community created in database
        cls.thirdC = Communaute.objects.get(id=2)

    def test_is_community_is_created(self):
        self.assertEqual(Communaute.objects.all().count(), 10)


class AllowedNumberTestCase(TestCase):
    """ TestCase for models AllowedNumber from student app """
    @classmethod
    def setUpClass(cls):
        # Create a bactch of AllowedNumber
        cls.allowNbs = AllowedNumberFactory.create_batch(200)

        # Get a allowed number from database
        cls.nb = AllowedNumber.objects.get(id=105)

    def test_if_allowed_numbers_are_created(self):
        self.assertEqual(AllowedNumber.objects.all().count(), 200)
