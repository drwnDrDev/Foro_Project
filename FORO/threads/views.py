from django.shortcuts import render

# Create your views here.
def threads(request):
    return render(request,"threads.html")
def thread(request):

    return render(request,"threads.html",{"thread":request.thread})