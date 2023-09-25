from django.shortcuts import render, redirect
from .models import Títulos, Ídolos, MaiorPublico23, Tabela, Task
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

@login_required
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

@login_required
def list_tasks(request):
  tasks = Task.objects.all()
  context = { "tasks": tasks }
  return render(request, "list_tasks.html", context=context)

@login_required
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

@login_required
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

@login_required
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

@login_required
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

@login_required
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

@login_required
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

@login_required
def delete_titulo(request, id):
  titul = Títulos.objects.get(id = id)
  if request.method == 'POST':
    if 'confirm' in request.POST:
      titul.delete()
    
    return redirect('home')
  return render(request, "are_you_titulo.html", context={'titul':titul})

@login_required
def delete_jogo(request, id):
  jog = MaiorPublico23.objects.get(id = id)
  if request.method == 'POST':
    if 'confirm' in request.POST:
      jog.delete()
    
    return redirect('home')
  return render(request, "are_you_jogo.html", context={'jog':jog})

@login_required
def delete_idolos(request, id):
  idolo = Ídolos.objects.get(id = id)
  if request.method == 'POST':
    if 'confirm' in request.POST:
      idolo.delete()
    
    return redirect('home')
  return render(request, "are_you_idolo.html", context={'idolo':idolo})

def create_user(request):
  if request.method == 'POST':
    user = User.objects.create_user(
    request.POST['username'],
    request.POST['email'],
    request.POST['password']
  )
    user.save()
    return redirect('home')
  return render(request, 'register.html', context={'action':'Adicionar'})

def login_user(request):
  if request.method == 'POST':
    user = authenticate(
      username = request.POST['username'],
      password = request.POST['password'])
    if user != None:
      login(request, user)
    else:
      return render(request, 'login.html', context={'error_msg':'Usuário não existe'})
    if request.user.is_authenticated:
      return redirect('home')
    return render(request, 'login.html', context={'error_msg':'Usuário não pode ser logado'})
  return render(request, 'login.html')

def logout_user(request):
  logout(request)
  return redirect('login')
