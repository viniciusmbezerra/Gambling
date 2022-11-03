from JogoDoBicho.views.imports import *

def cadastrar_conta(request):
    if request.method == "POST":
        formUsuario = UserCreateForm(request.POST)
        formCliente = ClienteForm(request.POST, request.FILES)
        if all((formUsuario.is_valid(), formCliente.is_valid())):
            usuario = formUsuario.save(commit=False)
            formUsuario.save()
            my_group = Group.objects.get(name='Clientes')
            usuario.groups.add(my_group)
            cliente = formCliente.save(commit=False)
            cliente.usuario = usuario
            formCliente.save()
            return redirect('ver_lances_jb')
    else:
        formUsuario = UserCreateForm()
        formCliente = ClienteForm()
    return render(request, 'custom/config_cliente.html', {'formUsuario': formUsuario, 'formCliente': formCliente})

def depositar(request):
    if isMembro(request.user, "Clientes"):
        if request.method == "POST":
            usuario = Cliente.objects.get(usuario__id=request.user.id)
            deposito = float(request.POST['valor'])
            if deposito > 0:
                usuario.saldo += deposito
                usuario.save()
                messages.success(request, 'Deposito realizado!!')
                return redirect('depositar_conta')
            else:
                messages.warning(request, 'Valor de deposito inválido!!')
                return redirect('depositar_conta')
        return render(request, 'custom/depositar.html', {})
    else:
        return redirect('ver_lances_jb')   

def sacar(request):
    if isMembro(request.user, "Clientes"):
        if request.method == "POST":
            usuario = Cliente.objects.get(usuario__id=request.user.id)
            try:
                saque = float(request.POST['valor'])
                if not(saque > usuario.saldo) and (saque != 0):
                    usuario.saldo -= saque
                    usuario.save()
                    messages.success(request, 'Saque realizado!!')
                    return redirect('sacar_conta')
                else:
                    messages.warning(request, 'Valor de saque inválido!!')
            except:
                messages.warning(request, 'Valor de saque inválido!!')
            return redirect('sacar_conta')
        return render(request, 'custom/saque.html', {})
    else:
        return redirect('ver_lances_jb')