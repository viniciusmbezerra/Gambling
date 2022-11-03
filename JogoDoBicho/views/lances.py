from JogoDoBicho.views.imports import *
from JogoDoBicho.templatetags import agendamento
import threading

def listar_categorias(request):
    if isMembro(request.user, 'Administradores'):
        categorias = Categoria.objects.all()
        return render(request, 'custom/listar_categorias.html', { 'categorias' : categorias })
    else:
        return redirect('ver_lances_jb')

def cadastrar_bicho(request):
    if isMembro(request.user, 'Administradores'):
        if request.method == "POST":
            formBicho = BichoForm(request.POST, request.FILES)
            if formBicho.is_valid():
                formBicho.save()
                return redirect('ver_bichos')
        
        else:
            formBicho = BichoForm()
            return render(request, 'custom/config_bicho.html', {'formBicho': formBicho})
    else:
        return redirect('ver_lances_jb')

def listar_bichos(request):
    if isMembro(request.user, 'Administradores'):
        bichos = Bicho.objects.all()
        return render(request, 'custom/listar_bichos.html', { 'bichos' : bichos })
    else:
        return redirect('ver_lances_jb')

def cadastrar_categoria(request):
    if isMembro(request.user, 'Administradores'):
        if request.method == "POST":
            formCategoria = CategoriaForm(request.POST)
            if formCategoria.is_valid():
                formCategoria.save()
                return redirect('ver_categorias')
        
        else:
            formCategoria = CategoriaForm()
            return render(request, 'custom/config_categoria.html', {'formCategoria': formCategoria})
    else:
        return redirect('ver_lances_jb')

def listar_lances_jb(request):
    lances = LanceJB.objects.all()
    if len(lances) <= 0:
        messages.warning(request, 'Não há lances')
    return render(request, 'custom/listar_lances.html', { 'lances' : lances })

def listar_lances_lt(request):
    lances = LanceLT.objects.all()
    return render(request, 'custom/listar_lances.html', { 'lances' : lances })

def detalhar_lance_jb(request, id):
    lance = get_object_or_404(LanceJB, pk=id)
    apostas = ApostaJB.objects.filter(lance__id=id)
    acumulativo = apostas.count() * lance.categoria.valor
    return render(request, 'custom/detalhar_lance.html', { 'lance' : lance, 'apostas' : apostas, 'acumulativo': acumulativo })

def detalhar_lance_lt(request, id):
    lance = get_object_or_404(LanceLT, pk=id)
    apostas = ApostaLT.objects.filter(lance__id=id)
    acumulativo = apostas.count() * lance.lance.categoria.valor
    return render(request, 'custom/detalhar_lance.html', { 'lance' : lance, 'apostas' : apostas, 'acumulativo': acumulativo })

def cadastrar_lance_jb(request):
    if isMembro(request.user, 'Administradores'):
        if request.method == "POST":
            formLanceJB = LanceJBForm(request.POST, request.FILES)
            if formLanceJB.is_valid():
                lance: LanceJB = formLanceJB.save(commit=False)
                lance.gerente = Administrador.objects.get(usuario__id=request.user.id)
                lance.save()
                formLanceJB.save()

                evento: Evento = Evento.objects.create(fim=lance.fim)
                evento.lance = lance
                evento.save()
                evento.verificarHora()
                
                messages.success(request, 'Lance criado!!')
                threading.Thread(target=agendamento).start()

                texto = f"O Lance {lance.id}# foi criado!! Voce tem ate {lance.fim}"
                Noticia.objects.create(descricao=texto).save()

                return redirect('ver_lances_jb')
            else:
                messages.warning(request, 'Lance inválido!!')
        else:
            formLanceJB = LanceJBForm()
        return render(request, 'custom/config_lance.html', {'formLanceJB': formLanceJB})
    else:
        return redirect('ver_lances_jb')

def ver_resultado(request, id):
    lance = get_object_or_404(LanceJB, pk=id)
    if lance.resultado == None:
        messages.warning(request, 'Resultado não gerado!!')
        return redirect('ver_lances_jb')
    else:
        return render(request, 'custom/listar_bichos.html', { 'bichos' : [lance.resultado] })