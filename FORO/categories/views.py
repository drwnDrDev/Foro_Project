from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def categories(request):
    return HttpResponse([1,2,3,4])