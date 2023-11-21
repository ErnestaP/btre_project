from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model): # we are extending base mode
    realtor = models.ForeignKey(Realtor, on_delete = models.DO_NOTHING) # what to do with realtor that is associated with this listing
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True) # blank=True means that this field it's optional
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1) # cannot be more than 99, can be like 1.5  bathroom
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField(default=0)
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')#we are defininf folder that we want to have inside media folder. All pics and files that we are uploading through admin area they goes to media folder
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank = True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank = True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank = True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank = True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank = True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title # the main field we wanna display in admin area


