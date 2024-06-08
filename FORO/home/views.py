from datetime import datetime
from django.shortcuts import render
from django.template import loader


def home(request):

    if datetime.now().hour < 12:
        jornada = "am"
    else:
        jornada = "pm"
    context={"jornada":jornada}
    return render(request, loader.get_template(home),context)
