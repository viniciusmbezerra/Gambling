from JogoDoBicho.views.imports import *

def ver_noticias(request):
    noticias = Noticia.objects.all().order_by('-id')
    if len(noticias) <= 0:
        messages.warning(request, "Não há noticias")
    return render(request, "custom/listar_noticias.html",{'noticias': noticias})
