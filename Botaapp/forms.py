from django import forms
#from .models import Títulos, Ídolos, MaiorPublico23, Tabela, Task

class Títulos(forms.ModelForm):
  IMPORTANCE=[
    ('M', 'Muito Importante'),
    ('I', 'Importante'),
    ('P', 'Pouco Importante'),
  ]
  WATCH=[
    ('A', 'Assisti'),
    ('N', 'Não assisti'),
    ('P', 'Não assisti todos')
  ]
  title = forms.CharField(max_length=50)
  importancia = forms.CharField(max_length=1, choices=IMPORTANCE, null=True)
  quantidade = forms.IntegerField(null=True)
  watched = forms.CharField(max_length=1, choices=WATCH, null=True)

class MaiorPublico23(forms.ModelForm):
  OPTIONS = [
    ('N', 'Não estive presente'),
    ('S', 'Estive presente'),
  ]
  title = forms.CharField(max_length=70)
  date = forms.DateField(null=True)
  publico = forms.IntegerField(null=True)
  presence = forms.CharField(max_length=1, choices=OPTIONS, null=True)
  
class Ídolos(forms.ModelForm):
  title = forms.CharField(max_length=50)
  position = forms.CharField(max_length=70, null=True)
  born_date = forms.DateField(null=True)
  birth_place = forms.CharField(max_length=50, null=True)

class Tabela(forms.ModelForm):
  name = forms.CharField(max_length=50)
  game = forms.IntegerField(null=True)
  position = forms.CharField(max_length=70, null=True)

class Task(forms.ModelForm):
  title = forms.CharField(max_length = 50)
  description = forms.TextField()
  due_date = forms.DateField()
  done = forms.BooleanField()

