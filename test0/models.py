from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from django.db import models
from django.utils import timezone 
from django.contrib.auth import get_user_model 
import os 
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
#from faker import Faker
#import faker.providers
#from django_faker import Faker
#populator = Faker.getPopulator()

#from django.core.files.storage import FileSystemStorage


#fs = FileSystemStorage(location='/home/ahmed/Downloads/success/d-s-main/static/wsite/coutries')

class Country(models.Model):
    name = models.CharField(max_length=255)      
    number_of_club = models.IntegerField()