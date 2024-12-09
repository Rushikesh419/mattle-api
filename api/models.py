from django.db import models

# Create your models here.
class Mattle(models.Model):
    product_name = models.CharField(max_length=50)
    product_description=models.CharField(max_length=400)
    product_type=models.CharField(max_length=100)
    product_url=models.CharField(max_length=200)
    product_img_link=models.CharField(max_length=200)