import os
import shutil

from django.conf import settings
from django.test import TestCase, override_settings
from student.factories.appartment_factory import AppartementFactory
from student.models.appartment_models import Appartment


@override_settings(MEDIA_ROOT=os.path.join(settings.BASE_DIR,
                                           'media_dir_for_test_appartment/'))
class AppartmentTestCase(TestCase):
    """ TestCase for Appartment models """
    @classmethod
    def setUpTestData(cls):
        # Create object appartment_factory in data
        cls.apparts = AppartementFactory.create_batch(10)

    def test_if_apparts_is_created(self):
        self.assertEqual(Appartment.objects.all().count(), 10)

    def test_if_appart_description_is_saved(self):
        self.assertEqual(f'{Appartment.objects.get(id=3).description}',
                         f'{self.apparts[2].description}')

    def test_if_appart_site_is_saved(self):
        self.assertEqual(f'{Appartment.objects.get(id=3).site}',
                         f'{self.apparts[2].site}')

    def test_if_appart_is_rented_is_saved(self):
        self.assertEqual(f'{Appartment.objects.get(id=3).is_rented}',
                         f'{self.apparts[2].is_rented}')

    def test_if_appart_lessor_name_is_saved(self):
        self.assertEqual(f'{Appartment.objects.get(id=3).lessor_name}',
                         f'{self.apparts[2].lessor_name}')

    def test_if_appart_lessor_number_is_saved(self):
        self.assertEqual(f'{Appartment.objects.get(id=3).lessor_number}',
                         f'{self.apparts[2].lessor_number}')

    def test_if_appart_image_is_saved(self):
        self.assertTrue(
            os.path.exists(f'{settings.MEDIA_ROOT}' +
                           f'{Appartment.objects.get(id=3).image}'))

    @classmethod
    def tearDownClass(cls):
        # Delete test media directory

        if os.path.exists(settings.MEDIA_ROOT):
            shutil.rmtree(settings.MEDIA_ROOT)

        super().tearDownClass()
