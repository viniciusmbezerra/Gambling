from django.urls import path
from JogoDoBicho.views import usuario, admin, cliente, lances, apostas, noticias

urlpatterns = [
    path('', noticias.ver_noticias, name="ver_noticias"),
    path('login/',usuario.logar, name="logar_usuario"),
    path('autenticar_usuario', usuario.autenticar_usuario, name='autenticar_usuario'),
    path('logout_usuario/', usuario.logout_usuario, name='logout_usuario'),
    path('perfil', usuario.ver_perfil, name="ver_perfil"),
    path('admins/ver', admin.listar_admins, name="ver_admins"),
    path('admins/buscar', admin.buscar_admins, name="buscar_admins"),
    path('admins/novo', admin.cadastrar_admin, name="cadastrar_admin"),
    path('clientes/ver', admin.listar_clientes, name="ver_clientes"),
    path('cliente/novo', cliente.cadastrar_conta, name="cadastrar_clientes"),
    path('cliente/depositar', cliente.depositar, name="depositar_conta"),
    path('cliente/sacar', cliente.sacar, name="sacar_conta"),
    path('categorias/ver', lances.listar_categorias, name="ver_categorias"),
    path('categorias/novo', lances.cadastrar_categoria, name="cadastrar_categoria"),
    path('bichos/ver', lances.listar_bichos, name="ver_bichos"),
    path('bicho/novo', lances.cadastrar_bicho, name="cadastrar_bicho"),
    path('lances/ver', lances.listar_lances_jb, name="ver_lances_jb"),
    path('lance/<int:id>/', lances.detalhar_lance_jb, name="detalhar_lance_jb"),
    path('lance/novo', lances.cadastrar_lance_jb, name="cadastrar_lance_jb"),
    path('lance/<int:id>/resultado/', lances.ver_resultado, name="ver_resultado"),
    path('apostas/ver', apostas.listar_apostas, name="ver_apostas"),
    path('aposta/novo/<int:id>', apostas.cadastrar_aposta_jb, name="cadastrar_aposta_jb"),
    path('apostas/my', apostas.listar_minhas_apostas, name="ver_minhas_apostas"),
    path('aposta/<int:id>/clientes/', apostas.listar_aposta_clientes, name="ver_aposta_clientes"),
]