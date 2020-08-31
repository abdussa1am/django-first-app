from django.db import models
from postgres_copy import CopyManager

# Create your models here.



class Crop(models.Model):
    domainc = models.CharField(max_length=500)
    domain = models.CharField(max_length=500)
    areac = models.IntegerField(null=True)
    area = models.CharField(max_length=500)
    elemc = models.IntegerField(null=True)
    elem =  models.CharField(max_length=500)
    itemc = models.IntegerField(null=True)
    item = models.CharField(max_length=500)
    yearc = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    unit = models.CharField(max_length=500)
    value = models.IntegerField(null=True)
    Flag = models.CharField(max_length=500 , null=True)
    Flagd = models.CharField(max_length=500)
    objects = CopyManager()
    class Meta:  
        db_table = "crop"
