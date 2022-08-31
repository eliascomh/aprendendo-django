from codecs import backslashreplace_errors
from datetime import datetime
from pyexpat import model
from tkinter.tix import Tree
from xml.sax import default_parser_list
from django.db import models


class Receita(models.Model):
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextChoices()
    modo_preparo = models.TextChoices()
    tempo_preparo = models.IntegerField()
    rendimento = models.TextField(max_length=100)
    categoria = models.CharField(max_length=100)
    date_receita = models.DateField(default=datetime.now, blank=True)
