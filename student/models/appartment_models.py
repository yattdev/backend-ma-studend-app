from django.db import models
from django_resized import ResizedImageField


# Create your models here.
class Appartment(models.Model):
    """Model that represent appartement in database"""
    description = models.TextField(blank=False)
    site = models.TextField(blank=False)
    is_rented = models.BooleanField(default=False)
    lessor_number = models.IntegerField(default="...", unique=True)
    lessor_name = models.CharField(max_length=255, blank=True, unique=True)
    image = ResizedImageField(size=[350, 280],
                              default='appartement-default.jpg',
                              crop=['left', 'rigth'],
                              upload_to='appartements_images')
