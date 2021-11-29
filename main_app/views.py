from django.contrib.auth.models import User

from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, DeleteView

from django.http import HttpResponse

from .models import Day

from .forms import DatingForm

from django.contrib.auth.views import LoginView

from django.contrib.auth import login

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required




class Home(LoginView):
  template_name = 'home.html'


def about(request):
  return render(request, 'about.html')


@login_required
def days_index(request):
  days = Day.objects.filter(user=request.user)
  return render(request, 'days/index.html', {'days': days })


@login_required
def days_detail(request, day_id):
  day = Day.objects.get(id=day_id)
  dating_form = DatingForm()
  return render(request, 'days/detail.html', {'day':day, 'dating_form': dating_form})



class DayCreate(LoginRequiredMixin, CreateView):
  model = Day
  fields = ['rating','mood', 'highs', 'lows', 'notes']
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)



class DayDelete(LoginRequiredMixin, DeleteView):
  model = Day
  success_url = '/days/'


@login_required
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