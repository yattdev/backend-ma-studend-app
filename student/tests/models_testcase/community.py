#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import shutil

from django.conf import settings
from django.test import TestCase, override_settings
from student.factories.utils_models_factory import CommunityFactory
from student.models.utils_models import Community


class CommunityTestCase(TestCase):
    """ TestCase for models Community from student app """
    @classmethod
    def setUpTestData(cls):
        # Create a bactch of Community
        cls.communautes = CommunityFactory.create_batch(10)

        # Fetch third community created in database
        cls.thirdC = Community.objects.get(id=2)

    def test_is_community_is_created(self):
        self.assertEqual(Community.objects.all().count(), 10)

    # This function is about to drop from database after TestCase
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
