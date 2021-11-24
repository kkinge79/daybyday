from django.db.models import fields

from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponse

from .models import Day




def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


def days_index(request):
  days = Day.objects.all()
  return render(request, 'days/index.html', {'days': days })

def days_detail(request, day_id):
  day = Day.objects.get(id=day_id)
  return render(request, 'days/detail.html', {'day':day})

class DayCreate(CreateView):
  model = Day
  fields = "__all__"

class DayUpdate(UpdateView):
  model = Day
  fields = ['rating', 'mood', 'highs', 'lows', 'notes']

class DayDelete(DeleteView):
  model = Day
  success_url = '/days/'
