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
    return render(request,'votes/votes.html',{'data':[	{"Club":"Once Caldas","PJPartidos jugados":10,"GTriunfos":7,"EEmpates":2,"PDerrotas":1,"GFGoles marcados":16,"GCGoles en contra":7,"DGDiferencia de goles":9,"PtsPuntos":23},{"Club":"América","PJPartidos jugados":8,"GTriunfos":6,"EEmpates":1,"PDerrotas":1,"GFGoles marcados":13,"GCGoles en contra":5,"DGDiferencia de goles":8,"PtsPuntos":19},{"Club":"Tolima","PJPartidos jugados":10,"GTriunfos":5,"EEmpates":2,"PDerrotas":3,"GFGoles marcados":15,"GCGoles en contra":8,"DGDiferencia de goles":7,"PtsPuntos":17},{"Club":"Fortaleza","PJPartidos jugados":10,"GTriunfos":4,"EEmpates":5,"PDerrotas":1,"GFGoles marcados":13,"GCGoles en contra":9,"DGDiferencia de goles":4,"PtsPuntos":17},{"Club":"Atlético Nacional","PJPartidos jugados":8,"GTriunfos":5,"EEmpates":1,"PDerrotas":2,"GFGoles marcados":12,"GCGoles en contra":7,"DGDiferencia de goles":5,"PtsPuntos":16},{"Club":"Millonarios","PJPartidos jugados":9,"GTriunfos":4,"EEmpates":2,"PDerrotas":3,"GFGoles marcados":13,"GCGoles en contra":9,"DGDiferencia de goles":4,"PtsPuntos":14},{"Club":"Pasto","PJPartidos jugados":9,"GTriunfos":4,"EEmpates":2,"PDerrotas":3,"GFGoles marcados":9,"GCGoles en contra":6,"DGDiferencia de goles":3,"PtsPuntos":14},{"Club":"Santa Fe","PJPartidos jugados":6,"GTriunfos":4,"EEmpates":1,"PDerrotas":1,"GFGoles marcados":8,"GCGoles en contra":4,"DGDiferencia de goles":4,"PtsPuntos":13},{"Club":"Águilas Doradas","PJPartidos jugados":8,"GTriunfos":3,"EEmpates":3,"PDerrotas":2,"GFGoles marcados":9,"GCGoles en contra":8,"DGDiferencia de goles":1,"PtsPuntos":12},{"Club":"Junior","PJPartidos jugados":8,"GTriunfos":3,"EEmpates":3,"PDerrotas":2,"GFGoles marcados":8,"GCGoles en contra":7,"DGDiferencia de goles":1,"PtsPuntos":12},{"Club":"La Equidad","PJPartidos jugados":9,"GTriunfos":3,"EEmpates":3,"PDerrotas":3,"GFGoles marcados":7,"GCGoles en contra":11,"DGDiferencia de goles":-4,"PtsPuntos":12},{"Club":"Deportivo Pereira","PJPartidos jugados":8,"GTriunfos":3,"EEmpates":1,"PDerrotas":4,"GFGoles marcados":5,"GCGoles en contra":6,"DGDiferencia de goles":-1,"PtsPuntos":10},{"Club":"Bucaramanga","PJPartidos jugados":9,"GTriunfos":3,"EEmpates":1,"PDerrotas":5,"GFGoles marcados":7,"GCGoles en contra":10,"DGDiferencia de goles":-3,"PtsPuntos":10},{"Club":"Alianza","PJPartidos jugados":8,"GTriunfos":2,"EEmpates":3,"PDerrotas":3,"GFGoles marcados":10,"GCGoles en contra":9,"DGDiferencia de goles":1,"PtsPuntos":9},{"Club":"Patriotas","PJPartidos jugados":10,"GTriunfos":2,"EEmpates":3,"PDerrotas":5,"GFGoles marcados":10,"GCGoles en contra":15,"DGDiferencia de goles":-5,"PtsPuntos":9},{"Club":"Medellín","PJPartidos jugados":8,"GTriunfos":1,"EEmpates":5,"PDerrotas":2,"GFGoles marcados":6,"GCGoles en contra":8,"DGDiferencia de goles":-2,"PtsPuntos":8},{"Club":"Deportivo Cali","PJPartidos jugados":9,"GTriunfos":2,"EEmpates":1,"PDerrotas":6,"GFGoles marcados":7,"GCGoles en contra":15,"DGDiferencia de goles":-8,"PtsPuntos":7},{"Club":"Jaguares","PJPartidos jugados":10,"GTriunfos":1,"EEmpates":3,"PDerrotas":6,"GFGoles marcados":2,"GCGoles en contra":10,"DGDiferencia de goles":-8,"PtsPuntos":6},{"Club":"Boyacá Chicó","PJPartidos jugados":9,"GTriunfos":1,"EEmpates":2,"PDerrotas":6,"GFGoles marcados":5,"GCGoles en contra":13,"DGDiferencia de goles":-8,"PtsPuntos":5},{"Club":"Envigado","PJPartidos jugados":8,"GTriunfos":1,"EEmpates":2,"PDerrotas":5,"GFGoles marcados":4,"GCGoles en contra":12,"DGDiferencia de goles":-8,"PtsPuntos":5}]})

def votes(request):
    return post