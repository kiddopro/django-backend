from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('all/', views.getAllPersons),
  path('<int:id>', views.getPerson)
]