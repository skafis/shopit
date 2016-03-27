from django.db import models
# Create your models here.
class Catalog(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150)
    publisher = models.CharField(max_length=300)
    description = models.TextField()
    #photo = models.ImageField(upload_to='product_photo', blank=True)
    price_in_dollars = models.DecimalField(max_digits=6, decimal_places=2)

