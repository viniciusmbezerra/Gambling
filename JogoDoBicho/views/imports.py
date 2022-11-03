from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from JogoDoBicho.models import  Administrador, Cliente, Categoria, Bicho, LanceJB, LanceLT, ApostaJB, ApostaLT, Evento
from JogoDoBicho.forms import UserCreateForm, AdministradorForm, ClienteForm, CategoriaForm, BichoForm, LanceJBForm, ApostaJBForm
from django.contrib import messages

def isMembro(usuario: User, grupo: str):
    return usuario.groups.filter(name=grupo).exists()