from django.urls import path

from . import views





urlpatterns = [

  path('', views.Home.as_view(), name='home'),

  path('about/', views.about, name='about'),

  path('days/', views.days_index, name="days_index"),

  path('days/<int:day_id>/', views.days_detail, name='days_detail'),

  path('days/create/', views.DayCreate.as_view(), name='days_create'),

  path('days/<int:pk>/delete/', views.DayDelete.as_view(), name="days_delete"),

  path ('accounts/signup/', views.signup, name='signup'),

]