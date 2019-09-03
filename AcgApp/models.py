from django.db import models
from django.conf import settings

# Create your models here.
class ContactTable(models.Model):
    firstname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message=models.TextField()

