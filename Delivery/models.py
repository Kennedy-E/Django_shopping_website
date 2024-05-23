from django.db import models

# Create your models here.
class Goods(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    price = models.FloatField()
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='home/')

