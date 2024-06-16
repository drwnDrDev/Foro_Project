from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    if datetime.now().hour < 12:
        jornada = "am"
    else:
        jornada = "pm"
    context = {"jornada":jornada}
    return render(request,'home/index.html',context)

def contact(request):
    contex={"title": "Contacto", "message": "Bienvenido a la pagina de contacto", "content":"Si tienes alguna duda o sugerencia, por favor no dudes en contactarnos",
            "darwin": {"phone": "1234567890","email": "dwd@yahoo.com"}, "carlos": {"phone": "0987654321","email": "fotoalep@gmail.com"}}
    return render(request,'home/contact.html',contex)
def about(request):
    return render(request,'home/about.html')
def threads_create(request):
    return render(request,'threads/create.html',{"user":1})
def threads(request):
    return render(request,'threads/index.html',{"data":[{"id":1,"user":1,"title":"Realmetente son necesarios estos mockups","create_at":datetime.now(),"update_at":datetime.now()},{"id":3,"user":2,"title":"Un usuario puede escribir varios theads","create_at":datetime.now(),"update_at":datetime.now()},{"id":2,"user":1,"title":"Las fechas interactuan con la vista o solo con el moedlo","create_at":datetime.now(),"update_at":datetime.now()}]})
def threads_show(request):
    return render(request,'threads/show.html',{"thread":{"id":1,"user":1,"title":"Realmetente son necesarios estos mockups","create_at":datetime.now(),"update_at":datetime.now()},"posts":[{"content":"Es realmente una perdida de tiempo en tareas poco productivas","user":1,"thread":1,"create_at":datetime.now(),"update_at":datetime.now()},{"content":"No, se pueden traer datos de prueba desde los kodelos i desde la base de datos de prueba","user":2,"thread":1,"create_at":datetime.now(),"update_at":datetime.now()} ]})
def threads_reply(request):
    return render(request,'threads/reply.html',{"thread":1})
def profile(request,user):    
    return render(request,'profile/index.html',{"user":{"id":1,"username":"Juanito Alimaña","email":"juanito123@example.com","create_at":datetime.now(),"update_at":datetime.now()}})