#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import shutil

from django.test import TestCase, override_settings
from student.models.student import Student
from student.factories.student_factory import StudentFactory
from django.conf import settings


@override_settings(MEDIA_ROOT=os.path.join(settings.BASE_DIR,
                                           "media_dir_for_studentTestCaste/"))
class StudentTestCase(TestCase):
    """ TestCase for Student models from from student app """
    @classmethod
    def setUpClass(cls):
        # Create a bactch of student
        cls.students = StudentFactory.create_batch(10)

        # Get to student from database
        cls.fourthStudent = Student.objects.get(id=3)

    def test_if_students_is_created(self):
        self.assertEqual(Student.objects.all().count(), 10)

    def test_if_student_image_is_saved(self):
        self.assertTrue(
            os.path.exists(f"{settings.MEDIA_ROOT}",
                           f"{self.fourthStudent.profile_image}"))

    @classmethod
    def tearDownClass(cls):
        # Detele media_dir_for_studentTestCaste

        if os.path.exists(settings.MEDIA_ROOT):
            shutil.rmtree(settings.MEDIA_ROOT)

        super().tearDownClass()
