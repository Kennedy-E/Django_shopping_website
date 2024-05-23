from django.db import models

# Create your models here.

class Goods(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='static/images')
    slug = models.SlugField(max_length=250, default=None)

    class Meta:
        verbose_name_plural = "Goods"
    def __str__(self):
        return self.name




