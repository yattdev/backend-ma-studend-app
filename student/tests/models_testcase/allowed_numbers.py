#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil

from django.conf import settings
from django.test import TestCase, override_settings
from student.factories.utils_models_factory import AllowedNumberFactory
from student.models.utils_models import AllowedNumber


class AllowedNumberTestCase(TestCase):
    """ TestCase for models AllowedNumber from student app """
    @classmethod
    def setUpTestData(cls):
        # Create a bactch of AllowedNumber
        cls.allowNbs = AllowedNumberFactory.create_batch(200)

        # Get a allowed number from database
        cls.nb = AllowedNumber.objects.get(id=cls.allowNbs[105].id)

    def test_if_allowed_numbers_are_created(self):
        self.assertEqual(AllowedNumber.objects.all().count(), 200)

    # This function is about to drop from database after TestCase
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
