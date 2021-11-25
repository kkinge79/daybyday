from django.forms import ModelForm
from .models import Dating

class DatingForm (ModelForm):
  class Meta:
    model = Dating
    fields = ['date', 'mood']