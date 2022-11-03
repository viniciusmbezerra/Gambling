from datetime import date, datetime, timedelta
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
import random
import ast
from JogoDoBicho.models import Cliente


class Concourse(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    draw_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    result = models.CharField(max_length=100, blank=True)
    collection = models.FloatField(blank=True, null=True)
    status = models.CharField(
            max_length=100,
            choices=[
                ('Open','Open'),
                ('Closed','Closed'),
            ],
            default='Open',
            )
    
    def collection_moment(self):
        delta = (self.draw_date - datetime.now())
        if (delta <= timedelta(days=0, hours=0, minutes=0, seconds=0, microseconds=0)) and self.status=='Open':
            self.gen_result()
        return Bet.objects.filter(concourse=self).count() * 4.5

    def add_scheduled_bet(self):
        objts = Bet.objects.filter(teimosinha__gt=0)
        for obj in objts:
            qtd = obj.concourse.count()
            if qtd <= int(obj.teimosinha):
                obj.concourse.add(self)
                obj.save()
    
    def gen_result(self):
        self.result = random.sample(range(1,61), 6)
        self.status = 'Closed'
        self.save()
        bets = Bet.objects.filter(concourse=self)
        for bet in bets:
            results = []
            games = ast.literal_eval(bet.surpresinha) if bet.surpresinha else []
            games.append(ast.literal_eval(bet.numbers))
            for g in games:
                g = [int(val) for val in g]
                cont=0
                for n in self.result:
                    if int(n) in g:
                        cont+=1
                results.append({'game': g,'correct': cont})
                if cont>0:
                    self.pay(bet.user.first())
            bet.results = results
            bet.save()
    
    def pay(self, winner):
        winner = Cliente.objects.filter(usuario=winner).first()
        winner.saldo += self.collection_moment()
        winner.save()


class Bet(models.Model):
    concourse = models.ManyToManyField(Concourse)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ManyToManyField(User)
    quantity_numbers = models.IntegerField()
    teimosinha = models.IntegerField()
    surpresinha = models.CharField(max_length=150, blank=True, null=True, default='')
    bet_type = models.CharField(
                max_length=10,
                choices=[
                    ('Simples', 'Simples'),
                    ('Bolão', 'Bolão'),
                ],
                default='Simples',
            )
    numbers = models.CharField(max_length=100,default='')
    value = models.FloatField(blank=True, null=True,default=4.5)
    results = models.CharField(max_length=300, blank=True, null=True)

    def gen_surpresinha(self, quant):
        aux = []
        for i in range(int(quant)):
            aux.append(random.sample(range(1,61), 6))
        self.surpresinha = aux
