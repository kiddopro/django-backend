from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Person

# Create your views here.
def index(request):
  print(request)
  return render(request, 'index.html')

def getAllPersons(request):
  person = Person.objects.all()
  return JsonResponse(list(person.values()), safe=False)

def getPerson(request, id):
  person = get_object_or_404(Person, id=id)
  n_person = {"name": person.name, "age": person.age}
  return JsonResponse(n_person, safe=False)
