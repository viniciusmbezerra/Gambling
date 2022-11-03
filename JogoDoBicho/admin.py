from django.contrib import admin
from JogoDoBicho.models import Administrador, Bicho, Categoria, LanceJB, LanceLT, ApostaJB, ApostaLT, Cliente, Premio, Evento

# Register your models here.
admin.site.register(Bicho)
admin.site.register(Administrador)
admin.site.register(Categoria)
admin.site.register(Evento)
admin.site.register(Premio)
admin.site.register(LanceJB)
admin.site.register(LanceLT)
admin.site.register(ApostaJB)
admin.site.register(ApostaLT)
admin.site.register(Cliente)