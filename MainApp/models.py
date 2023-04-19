from django.db import models


class Item(models.Model):
    name  = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    desc = models.CharField(max_length=1500, default='')
    #def __str__(self) -> str:
     # return self.name, self.brand, self.count
