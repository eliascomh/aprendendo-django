from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', view.login, name='login'),
    path('dashboard', view.dashboard, name='dashboard')
    path('logout', views.logout, name='logout')

]
