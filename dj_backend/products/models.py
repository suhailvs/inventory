from django.db import models
from django.utils import timezone
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    #quantity = models.IntegerField(default=0)
    created_date = models.DateTimeField('date created', default=timezone.now)
    def __str__(self):
        return "#%d: %s -> %d" %(self.id, self.name,self.price)
