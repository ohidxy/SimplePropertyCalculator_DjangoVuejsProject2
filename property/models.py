from django.db import models

class PropertyType(models.Model):
    type_name = models.CharField(max_length=255)

# Create your models here.
class Property(models.Model):
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    property_name = models.CharField(max_length=255)
    land_area = models.FloatField()
    transaction_price = models.FloatField()
    data = models.DateField()