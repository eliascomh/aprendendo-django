from nturl2path import url2pathname
from django.urls import path

from . import views

urlpattens = [
    path('', views.index, name=index)

]
