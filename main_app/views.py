from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, DeleteView

from django.http import HttpResponse

from .models import Day

from .forms import DatingForm


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


def days_index(request):
  days = Day.objects.all()
  return render(request, 'days/index.html', {'days': days })

def days_detail(request, day_id):
  day = Day.objects.get(id=day_id)
  dating_from = DatingForm()
  return render(request, 'days/detail.html', {'day':day, 'dating_form': dating_from})

class DayCreate(CreateView):
  model = Day
  fields = "__all__"

class DayDelete(DeleteView):
  model = Day
  success_url = '/days/'
