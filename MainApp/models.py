from django.db import models


class Color(models.Model):
   name  = models.CharField(max_length=20)
   def __str__(self) -> str:
      return f"{self.name}"

class Item(models.Model):
    name  = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    desc = models.CharField(max_length=1500, default='')
    colors = models.ManyToManyField(to=Color)
    def __str__(self) -> str:
      return f"{self.name, self.brand, self.count}"



