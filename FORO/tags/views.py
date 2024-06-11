from django.shortcuts import render

# Create your views here.
def tags(request):
    return render(request,"tags.html")