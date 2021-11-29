from django.db import models

from django.urls import reverse

from datetime import date

from django.utils import timezone

from django.contrib.auth.models import User

from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Day(models.Model):
  date = models.DateField(default=timezone.now)
  rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)])
  mood = models.CharField(max_length=100)
  highs = models.CharField(max_length=100)
  lows = models.CharField(max_length=100)
  notes = models.TextField(max_length=1000)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def get_absolute_url(self):
    return reverse('days_detail', kwargs={'day_id': self.id})

  class Meta:
    ordering = ['-date']

