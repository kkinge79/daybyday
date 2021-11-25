from django.contrib import admin

# Register your models here.
from .models import Day, Dating

admin.site.register(Day)

admin.site.register(Dating)