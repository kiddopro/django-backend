from django.db import models

class Person(models.Model):
  name = models.CharField(max_length=30)
  age = models.IntegerField()

class Car(models.Model):
  name = models.CharField(max_length=30)
  color = models.CharField(max_length=30)
  person = models.ForeignKey(Person, on_delete=models.CASCADE)