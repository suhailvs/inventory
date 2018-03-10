from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	price = models.IntegerField(default=0)
	#quantity = models.IntegerField(default=0)
	def __str__(self):
		return "#%d: %s -> %d" %(self.id, self.name,self.price)
