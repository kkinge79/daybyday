from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render

from .models import Day


# class Day:
#   def __init__(self, rating, mood, highs, lows, notes ):
#     self.rating = rating
#     self.mood = mood
#     self.highs = highs
#     self.lows = lows
#     self.notes = notes
# Create your views here.

# days = [
#   Day(9, 'happy', 'free coffee', 'lost my favorite pen', 'nothing else to add'),
#   Day(3, 'sad', 'good soup', 'bad drinks', 'nothing to add'),
#   Day(5, 'sad', 'good soup', 'bad drinks', 'nothing to add')
# ]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


def days_index(request):
  days = Day.objects.all()
  return render(request, 'days/index.html', {'days': days })
