from django.db import models

class Títulos(models.Model):
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
  title = models.CharField(max_length=50)
  importancia = models.CharField(max_length=1, choices=IMPORTANCE, null=True)
  quantidade = models.IntegerField(null=True)
  watched = models.CharField(max_length=1, choices=WATCH, null=True)

class MaiorPublico23(models.Model):
  OPTIONS = [
    ('N', 'Não estive presente'),
    ('S', 'Estive presente'),
  ]
  title = models.CharField(max_length=70)
  date = models.DateField(null=True)
  publico = models.IntegerField(null=True)
  presence = models.CharField(max_length=1, choices=OPTIONS, null=True)
  
class Ídolos(models.Model):
  title = models.CharField(max_length=50)
  position = models.CharField(max_length=70, null=True)
  born_date = models.DateField(null=True)
  birth_place = models.CharField(max_length=50, null=True)

class Tabela(models.Model):
  name = models.CharField(max_length=50)
  game = models.IntegerField(null=True)
  position = models.CharField(max_length=70, null=True)

class Task(models.Model):
  title = models.CharField(max_length = 50)
  description = models.TextField()
  due_date = models.DateField()
  done = models.BooleanField()
