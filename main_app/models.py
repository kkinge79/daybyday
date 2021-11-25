from django.db import models

from django.urls import reverse

from django.contrib.auth.models import User
# Create your models here.
MOOD = (
  ('G', '😊'),
  ('N', '😐'),
  ('B', '😢'),
  ('A', '😡'),
)

class Day(models.Model):
  rating = models.IntegerField()
  mood = models.CharField(max_length=100)
  highs = models.CharField(max_length=100)
  lows = models.CharField(max_length=100)
  notes = models.TextField(max_length=1000)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def get_absolute_url(self):
    return reverse('days_detail', kwargs={'day_id': self.id})

class Dating(models.Model):
  date = models.DateField('Date')
  mood = models.CharField(max_length=1, choices= MOOD, default=MOOD[0][0])

  day = models.ForeignKey(Day, on_delete=models.CASCADE)

  def __str__(self):
      return f"{self.get_mood_display()} on {self.date}"
    
  class Meta:
    ordering = ['-date']