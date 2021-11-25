from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, DeleteView

from django.http import HttpResponse

from .models import Day

from .forms import DatingForm

from django.contrib.auth.views import LoginView

from django.contrib.auth import login

from django.contrib.auth.forms import UserCreationForm

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
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

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


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('days_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)