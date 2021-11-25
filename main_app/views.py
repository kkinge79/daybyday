from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, DeleteView

from django.http import HttpResponse

from .models import Day

from .forms import DatingForm

from django.contrib.auth.views import LoginView

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')


def days_index(request):
  days = Day.objects.all()
  return render(request, 'days/index.html', {'days': days })

def days_detail(request, day_id):
  day = Day.objects.get(id=day_id)
  dating_form = DatingForm()
  return render(request, 'days/detail.html', {'day':day, 'dating_form': dating_form})

class DayCreate(CreateView):
  model = Day
  fields = "__all__"

class DayDelete(DeleteView):
  model = Day
  success_url = '/days/'

def add_dating(request, day_id):
  form = DatingForm(request.POST)
  if form.is_valid():
    new_dating = form.save(commit=False)
    new_dating.day_id = day_id
    new_dating.save()
  return redirect('days_detail', day_id=day_id)
