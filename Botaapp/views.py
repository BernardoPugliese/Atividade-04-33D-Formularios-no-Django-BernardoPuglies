from django.shortcuts import render, redirect
from .models import Títulos, Ídolos, MaiorPublico23, Tabela, Task
#from .forms import Títulos, Ídolos, MaiorPublico23, Tabela, Task

def home(request):
  titulos = Títulos.objects.all()
  idols = Ídolos.objects.all()
  publics = MaiorPublico23.objects.all()
  tables = Tabela.objects.all()
  
  return render(request, "home.html", context={
    'titulos':titulos, 
    'idols':idols, 
    'publics':publics,
    'tables':tables,
  })

def list_tasks(request):
  tasks = Task.objects.all()
  context = { "tasks": tasks }
  return render(request, "list_tasks.html", context=context)

def create_titulo(request):
  if request.method == 'POST':
    Títulos.objects.create(
      title = request.POST['title'],
      importancia = request.POST['importancia'],
      quantidade = request.POST['quantidade'],
      watched = request.POST['watched']
    )
    return redirect('home')
  return render(request, "titulo_form.html", context={'type':'Adicionar'})

def create_jogo(request):
  if request.method == 'POST':
    MaiorPublico23.objects.create(
      title = request.POST['title'],
      date = request.POST['date'],
      publico = request.POST['publico'],
      presence = request.POST['presence']
    )
    return redirect('home')
  return render(request, "jogo_form.html", context={'type':'Adicionar'})

def create_idolos(request):
  if request.method == 'POST':
    Ídolos.objects.create(
      title = request.POST['title'],
      position = request.POST['position'],
      born_date = request.POST['born_date'],
      birth_place = request.POST['birth_place']
    )
    return redirect('home')
  return render(request, "idolo_form.html", context={'type':'Adicionar'})

def update_titulo(request, id):
  titul = Títulos.objects.get(id = id)
  if request.method == 'POST':
    titul.title = request.POST['title']
    titul.importancia = request.POST['importancia']
    titul.quantidade = request.POST['quantidade']
    titul.watched = request.POST['watched']
    titul.save()
    
    return redirect('home')
  return render(request, "titulo_form.html", context={'type':'Atualizar', 'titul':titul})

def update_jogo(request, id):
  jog = MaiorPublico23.objects.get(id = id)
  if request.method == 'POST':
    jog.title = request.POST['title']
    jog.date = request.POST['date']
    jog.publico = request.POST['publico']
    jog.presence = request.POST['presence']
    jog.save()
    
    return redirect('home')
  return render(request, "jogo_form.html", context={'type':'Atualizar', 'jog':jog})

def update_idolos(request, id):
  idolo = Ídolos.objects.get(id = id)
  if request.method == 'POST':
    idolo.title = request.POST['title']
    idolo.position = request.POST['position']
    idolo.born_date = request.POST['born_date']
    idolo.birth_place = request.POST['birth_place']
    idolo.save()
    
    return redirect('home')
  return render(request, "idolo_form.html", context={'type':'Atualizar', 'idolo':idolo})

def delete_titulo(request, id):
  titul = Títulos.objects.get(id = id)
  if request.method == 'POST':
    if 'confirm' in request.POST:
      titul.delete()
    
    return redirect('home')
  return render(request, "are_you_titulo.html", context={'titul':titul})

def delete_jogo(request, id):
  jog = MaiorPublico23.objects.get(id = id)
  if request.method == 'POST':
    if 'confirm' in request.POST:
      jog.delete()
    
    return redirect('home')
  return render(request, "are_you_jogo.html", context={'jog':jog})

def delete_idolos(request, id):
  idolo = Ídolos.objects.get(id = id)
  if request.method == 'POST':
    if 'confirm' in request.POST:
      idolo.delete()
    
    return redirect('home')
  return render(request, "are_you_idolo.html", context={'idolo':idolo})