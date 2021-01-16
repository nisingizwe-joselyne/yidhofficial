from rest_framework import serializers
from .models import*

class RecordSerializer(serializers.ModelSerializer):
   class Meta:
       model = Record
       depth = 1 
       fields = ('__all__')

class CoopeSerializer(serializers.ModelSerializer):
   class Meta:
       model = Cooperatives
       depth = 1 
       fields = ('__all__')       

class FarmerSerializer(serializers.ModelSerializer):
   class Meta:
       model = Farmers
       depth = 1 
       fields = ('__all__')       