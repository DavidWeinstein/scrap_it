from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Materials

# Create your views here.
def index(request):
    return HttpResponse("Hello world, we are at the Scrap It index page.")

def detail(request, materials_id):
    return HttpResponse("The material is %s." % Materials.material_name)
