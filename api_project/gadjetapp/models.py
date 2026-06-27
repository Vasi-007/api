from django.db import models

# Create your models here.
class Gadjet(models.Model):
  title = models.CharField(max_length=100)
  brand = models.CharField(max_length=50)
  price = models.FloatField()
  warranty_years = models.IntegerField()

  def __str__(self):
    return self.title
