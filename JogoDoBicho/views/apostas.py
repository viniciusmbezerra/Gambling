from JogoDoBicho.views.imports import *

def cadastrar_aposta_jb(request, id):
    if isMembro(request.user, 'Clientes'):
        if request.method == "POST":
            lance = LanceJB.objects.get(id=id)
            formApostaJB = ApostaJBForm(request.POST, request.FILES)
            if formApostaJB.is_valid() and lance.estado != 'Encerrado':
                aposta: ApostaJB = formApostaJB.save(commit=False)
                aposta.lance = lance
                aposta.cliente = Cliente.objects.get(usuario__id=request.user.id)
                try:
                    valor = float(aposta.lance.categoria.valor)
                    if not(valor > aposta.cliente.saldo) and (valor != 0):
                        aposta.cliente.saldo -= valor
                        formApostaJB.save()
                        aposta.cliente.save()
                        messages.success(request, 'Aposta feita!!')
                        return redirect('ver_lances_jb')
                    else:
                        messages.success(request, 'Você não possui saldo suficiente!!')
                except:
                    messages.warning(request, 'Não foi possivel realizar a aposta!!')
                    return redirect('ver_lances_jb')
            else:
                messages.warning(request, 'Não foi possivel realizar a aposta!!')
                return redirect('ver_lances_jb')
        else:
            formApostaJB = ApostaJBForm()
        return render(request, 'custom/config_aposta.html', {'formApostaJB': formApostaJB})
    else:
        return redirect('ver_lances_jb')

def listar_apostas(request):
    if isMembro(request.user, 'Administradores'):
        apostas = ApostaJB.objects.all()
        return render(request, 'custom/listar_apostas.html', { 'apostas' : apostas })
    elif isMembro(request.user, 'Clientes'):
        return redirect('ver_minhas_apostas')
    else:
        return redirect('ver_apostas')

def listar_aposta_clientes(request, id):
    lance_ = get_object_or_404(LanceJB, pk=id)
    if isMembro(request.user, 'Administradores'):
        apostas = ApostaJB.objects.filter(lance=lance_)
        if len(apostas) > 0:
            return render(request, 'custom/listar_apostas.html', { 'apostas' : apostas })
        else:
            messages.warning(request, "Nenhum aposta foi feita!")
            return redirect('ver_lances_jb')
    else:
        return redirect('ver_lances_jb')

def listar_minhas_apostas(request):
    if isMembro(request.user, 'Clientes'):
        try:
            cliente = Cliente.objects.get(usuario__id=request.user.id)
            apostas = ApostaJB.objects.filter(cliente__id=cliente.id)
            if len(apostas) <= 0:
                messages.warning(request, 'Você não tem novas apostas')
            return render(request, 'custom/listar_apostas.html', { 'apostas' : apostas })
        except:
            return redirect('ver_apostas')
    else:
        return redirect('ver_apostas')
