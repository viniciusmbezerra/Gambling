from JogoDoBicho.views.imports import *

def listar_clientes(request):
    if isMembro(request.user, 'Administradores'):
        clientes = Cliente.objects.all()
        return render(request, 'custom/listar_clientes.html', { 'clientes' : clientes })
    else:
        return redirect('ver_lances_jb')

def listar_admins(request):
    if isMembro(request.user, 'Administradores'):
        admins = Administrador.objects.all()
        return render(request, 'custom/listar_administradores.html', { 'admins' : admins })
    else:
        return redirect('ver_lances_jb')

def buscar_admins(request):
    if isMembro(request.user, 'Administradores'):
        admins = Administrador.objects.all()
        if request.POST['info'] != '':
            info = request.POST['info']
            admins = admins.filter(usuario__username__contains=info) 
        if request.POST['nome'] != '':
            admins = admins.order_by(request.POST['nome'])
        if request.POST['email'] != '':
            admins = admins.order_by(request.POST['email'])
        return render(request, 'custom/listar_administradores.html', { 'admins' : admins })
    else:
        return redirect('ver_lances_jb')

def cadastrar_admin(request):
    if request.method == "POST":
        formUsuario = UserCreateForm(request.POST)
        formAdministrador = AdministradorForm(request.POST, request.FILES)
        if all((formUsuario.is_valid(), formAdministrador.is_valid())):
            usuario = formUsuario.save(commit=False)
            formUsuario.save()
            my_group = Group.objects.get(name='Administradores')
            usuario.groups.add(my_group)
            Administrador = formAdministrador.save(commit=False)
            Administrador.usuario = usuario
            formAdministrador.save()
            return redirect('ver_lances_jb')
    else:
        formUsuario = UserCreateForm()
        formAdministrador = AdministradorForm()
    return render(request, 'custom/config_administrador.html', {'formUsuario': formUsuario, 'formAdministrador': formAdministrador})
