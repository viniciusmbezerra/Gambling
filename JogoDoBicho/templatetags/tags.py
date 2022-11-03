from django import template 
from JogoDoBicho.models import Cliente, Administrador
register = template.Library() 

@register.simple_tag
def saldoCliente(id):
    return Cliente.objects.get(usuario__id=id).saldo

@register.simple_tag
def imgCliente(id):
    try:
        return Cliente.objects.get(usuario__id=id).foto.url
    except:
        return Administrador.objects.get(usuario__id=id).foto.url