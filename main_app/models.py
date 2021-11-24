from django.db import models

# Create your models here.
class Day(models.Model):
  rating = models.IntegerField()
  mood = models.CharField(max_length=100)
  highs = models.CharField(max_length=100)
  lows = models.CharField(max_length=100)
  notes = models.CharField(max_length=1000)

  # def __str__(self):
  #     return self.name