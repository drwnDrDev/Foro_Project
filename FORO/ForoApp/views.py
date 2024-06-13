from django.shortcuts import render
from datetime import datetime

# Create your views here.

def home(request):

    if datetime.now().hour < 12:
        jornada = "am"
    else:
        jornada = "pm"
    context={"jornada":jornada}
    return render(request,'home/index.html',context)

def contact(request):
    contex={"title": "Contacto", "message": "Bienvenido a la pagina de contacto", "content":"Si tienes alguna duda o sugerencia, por favor no dudes en contactarnos",
            "darwin": {"phone": "1234567890","email": "dwd@yahoo.com"}, "carlos": {"phone": "0987654321","email": "fotoalep@gmail.com"}}
    return render(request,'home/contact.html',contex)
def about(request):
    return render(request,'home/about.html')