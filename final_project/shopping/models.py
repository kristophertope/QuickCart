from django.db import models

# Create your models here.
class inventory_items(models.Model):
    item_number = models.CharField(primary_key=True, max_length=3)
    item_name = models.CharField(max_length=50)
    item_price = models.DecimalField(max_digits=5, decimal_places=2)
    item_description = models.CharField(max_length=1000)
    item_image = models.ImageField(null = True, blank = True, upload_to="images/")

