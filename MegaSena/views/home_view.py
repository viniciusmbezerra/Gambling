from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from MegaSena.forms import BetForm
from MegaSena.models import Bet, Concourse


@login_required(login_url='JogoDoBicho:logar_usuario', redirect_field_name='next')
def home(request):
    concourses = Concourse.objects.all().order_by('-id')

    return render(request, 'MegaSena/pages/home.html', {
        'concourses': concourses,
    })


@login_required(login_url='JogoDoBicho:logar_usuario', redirect_field_name='next')
def bet(request, id):
    numbers = []
    for n in range(1,61):
        if n < 10:
            numbers.append("0"+str(n))
        else:
            numbers.append(str(n))
    quant_numbers_options = []
    for n in range(6,16):
        if n < 10:
            quant_numbers_options.append("0"+str(n))
        else:
            quant_numbers_options.append(str(n))
    surpresinha_options = ['00']
    for n in range(1,8):
        if n < 10:
            surpresinha_options.append("0"+str(n))
        else:
            surpresinha_options.append(str(n))
    teimosinha_options = ['00','02', '04', '08']

    if request.POST:
        bet = Bet()
        bet.numbers = request.POST.get('numbers')
        bet.quantity_numbers = request.POST.get('quantity_numbers')
        bet.teimosinha = request.POST.get('teimosinha')
        bet.numbers = request.POST.getlist('numbers')
        bet.save()
        bet.gen_surpresinha(request.POST.get('surpresinha'))
        bet.concourse.add(Concourse.objects.get(id=id))
        bet.user.add(request.user)
        bet.save()

        messages.success(request, 'Saved successfully')
        return redirect(reverse('MegaSena:bet', args=(id,)))

    return render(request, 'MegaSena/pages/bet.html', {
        'id_concourse': id,
        'numbers': numbers,
        'quant_numbers_options': quant_numbers_options,
        'surpresinha_options': surpresinha_options,
        'teimosinha_options': teimosinha_options,
    })


@login_required(login_url='JogoDoBicho:logar_usuario', redirect_field_name='next')
def my_bets(request):
    bets = Bet.objects.filter(user=request.user)

    return render(request, 'MegaSena/pages/my_bets.html', {'bets':bets})
