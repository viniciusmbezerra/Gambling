from JogoDoBicho.views.imports import *

def autenticar_usuario(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('ver_lances_jb')
    else:
        return render(request, 'custom/login.html', {})

def logar(request):
    return render(request, 'custom/login.html', {})

def logout_usuario(request):
    logout(request)
    return redirect('ver_lances_jb')

def ver_perfil(request):
    if isMembro(request.user, 'Administradores'):
        admin = Administrador.objects.get(usuario__id=request.user.id)
        formUsuario = UserCreateForm(instance=admin.usuario)
        formAdministrador = AdministradorForm(instance=admin)
        return render(request, 'custom/perfil.html', { 'perfil': admin, 'formUsuario': formUsuario, 'formPerfil': formAdministrador})
    if isMembro(request.user, 'Clientes'):
        cliente = Cliente.objects.get(usuario__id=request.user.id)
        formUsuario = UserCreateForm(instance=cliente.usuario)
        formCliente = ClienteForm(instance=cliente)
        return render(request, 'custom/perfil.html', { 'perfil': cliente, 'formUsuario': formUsuario, 'formPerfil': formCliente})
    else:
        return redirect('logar_usuario')
