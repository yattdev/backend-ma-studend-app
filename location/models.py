from django.db import models
from django.shortcuts import reverse
from accounts.models import Owner,Agent,Guest


# Create your models here.
class Amenity(models.Model):
    name=models.CharField(max_length=128)
    def __str__(self):
        return self.name

class Apartment(models.Model):
    name= models.CharField(max_length=128)
    slug= models.SlugField(max_length=128)
    adresse= models.CharField(max_length=128)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='apartment',blank=True,null=True)
    city = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    bed_rooms= models.IntegerField(default=0)
    bath_rooms=models.IntegerField(default=0)
    max_guests=models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    is_available= models.BooleanField(default=True)
    area=models.FloatField(default=0.0)
    garage=models.IntegerField(default=0)
    amenities = models.ManyToManyField(Amenity)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE,null=True)
    agent= models.ForeignKey(Agent, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('apartment',kwargs={'slug':self.slug})

class Reservation(models.Model):
    guest=models.ForeignKey(Guest,on_delete=models.CASCADE,null=True)
    apartment=models.ForeignKey(Apartment,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField()
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    is_confirmed=models.BooleanField(default=False)
    is_paid=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.apartment.name} est loué par {self.guest.username}"