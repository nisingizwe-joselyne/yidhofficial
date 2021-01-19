
from django.db import models

# Create your models here.
class Farmers(models.Model):
    names = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.names
class Cooperatives(models.Model):
    name= models.CharField(max_length=40)
    leader = models.CharField(max_length=40)
    harvesting_type = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    farmers = models.CharField(max_length=45)
    description = models.TextField()
    def __str__(self):
        return self.name
class Record(models.Model):
    date  = models.DateTimeField(auto_now_add=True)
    cooperative = models.ForeignKey( Cooperatives, on_delete=models.CASCADE)
    farmer = models.ForeignKey( Farmers, on_delete=models.CASCADE)
    Quantity = models.CharField(max_length=40)
    phone = models.CharField(max_length=45)
   
    def __str__(self):
        return self.farmer