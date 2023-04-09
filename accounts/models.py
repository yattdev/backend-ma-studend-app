from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone_number=models.IntegerField(null=True)
    image=models.ImageField(upload_to='Agent',blank=True,null=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        verbose_name="User"
class Guest(User):
    class Meta:
        verbose_name="Guest"
class Owner(User):
    class Meta:
        verbose_name="Owner"
class Agent(User):
    class Meta:
        verbose_name="Agent"
