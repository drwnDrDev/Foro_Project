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
def profile_new(request):
    return render(request,'profile/create.html',{})
def profile_edit(request,user):
    return render(request,'profile/edit.html',{})
def profile_delete(request,user):
    return render(request,'profile/delete.html',{})

def politica_de_datos(request):
    return render(request,'home/tratamiento_de_datos.html',{})

def votes(request):
    return render(request,'votes/votes.html',{'data':[	{"club":"Once Caldas","PJ":10,"GTriunfos":7,"EEmpates":2,"PDerrotas":1,"GF":16,"GC":7,"DG":9,"PtsPuntos":23},{"club":"América","PJ":8,"GTriunfos":6,"EEmpates":1,"PDerrotas":1,"GF":13,"GC":5,"DG":8,"PtsPuntos":19},{"club":"Tolima","PJ":10,"GTriunfos":5,"EEmpates":2,"PDerrotas":3,"GF":15,"GC":8,"DG":7,"PtsPuntos":17},{"club":"Fortaleza","PJ":10,"GTriunfos":4,"EEmpates":5,"PDerrotas":1,"GF":13,"GC":9,"DG":4,"PtsPuntos":17},{"club":"Atlético Nacional","PJ":8,"GTriunfos":5,"EEmpates":1,"PDerrotas":2,"GF":12,"GC":7,"DG":5,"PtsPuntos":16},{"club":"Millonarios","PJ":9,"GTriunfos":4,"EEmpates":2,"PDerrotas":3,"GF":13,"GC":9,"DG":4,"PtsPuntos":14},{"club":"Pasto","PJ":9,"GTriunfos":4,"EEmpates":2,"PDerrotas":3,"GF":9,"GC":6,"DG":3,"PtsPuntos":14},{"club":"Santa Fe","PJ":6,"GTriunfos":4,"EEmpates":1,"PDerrotas":1,"GF":8,"GC":4,"DG":4,"PtsPuntos":13},{"club":"Águilas Doradas","PJ":8,"GTriunfos":3,"EEmpates":3,"PDerrotas":2,"GF":9,"GC":8,"DG":1,"PtsPuntos":12},{"club":"Junior","PJ":8,"GTriunfos":3,"EEmpates":3,"PDerrotas":2,"GF":8,"GC":7,"DG":1,"PtsPuntos":12},{"club":"La Equidad","PJ":9,"GTriunfos":3,"EEmpates":3,"PDerrotas":3,"GF":7,"GC":11,"DG":-4,"PtsPuntos":12},{"club":"Deportivo Pereira","PJ":8,"GTriunfos":3,"EEmpates":1,"PDerrotas":4,"GF":5,"GC":6,"DG":-1,"PtsPuntos":10},{"club":"Bucaramanga","PJ":9,"GTriunfos":3,"EEmpates":1,"PDerrotas":5,"GF":7,"GC":10,"DG":-3,"PtsPuntos":10},{"club":"Alianza","PJ":8,"GTriunfos":2,"EEmpates":3,"PDerrotas":3,"GF":10,"GC":9,"DG":1,"PtsPuntos":9},{"club":"Patriotas","PJ":10,"GTriunfos":2,"EEmpates":3,"PDerrotas":5,"GF":10,"GC":15,"DG":-5,"PtsPuntos":9},{"club":"Medellín","PJ":8,"GTriunfos":1,"EEmpates":5,"PDerrotas":2,"GF":6,"GC":8,"DG":-2,"PtsPuntos":8},{"club":"Deportivo Cali","PJ":9,"GTriunfos":2,"EEmpates":1,"PDerrotas":6,"GF":7,"GC":15,"DG":-8,"PtsPuntos":7},{"club":"Jaguares","PJ":10,"GTriunfos":1,"EEmpates":3,"PDerrotas":6,"GF":2,"GC":10,"DG":-8,"PtsPuntos":6},{"club":"Boyacá Chicó","PJ":9,"GTriunfos":1,"EEmpates":2,"PDerrotas":6,"GF":5,"GC":13,"DG":-8,"PtsPuntos":5},{"club":"Envigado","PJ":8,"GTriunfos":1,"EEmpates":2,"PDerrotas":5,"GF":4,"GC":12,"DG":-8,"PtsPuntos":5}]})
