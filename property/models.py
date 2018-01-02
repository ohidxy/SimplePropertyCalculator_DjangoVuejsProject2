from django.db import models

class PropertyType(models.Model):
    type_name = models.CharField(max_length=255)

    def __str__(self):
      return self.type_name


class Property(models.Model):
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    property_name = models.CharField(max_length=255)
    property_address = models.CharField(max_length=255)
    land_area = models.FloatField()
    transaction_price = models.FloatField()
    price_per_ft2 = models.FloatField(editable=False)
    date = models.DateField()
    built_up_area = models.FloatField()

    def save(self):
      self.price_per_ft2 = self.transaction_price / self.land_area
      return super(Property, self).save() 

    def __str__(self):
      return self.property_name