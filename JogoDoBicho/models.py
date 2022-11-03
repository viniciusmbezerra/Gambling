import random
from django.db import models
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User, Group


class Administrador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    data_nasc = models.DateField(null=True, blank=True, verbose_name='Data de Nascimento')
    foto = models.ImageField(upload_to='JogoDoBicho/src/img/pessoas', blank=True, default='static/dist/img/anonimo.png')
    
    def __str__(self):
        return self.usuario.username

    def idade(self):
        return date.today().year - self.data_nasc.year

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    data_nasc = models.DateField(null=True, blank=True, verbose_name='Data de Nascimento')
    foto = models.ImageField(upload_to='JogoDoBicho/src/img/pessoas', blank=True, default='static/dist/img/anonimo.png')
    saldo = models.FloatField(default=0.0)

    def __init__(self, *args, **kwargs):
        try:
            Group.objects.get(name='Clientes')
        except:
            grupo = Group.objects.create(name='Clientes')
            grupo.permissions.set([
                'JogoDoBicho.view_bicho',
                'JogoDoBicho.view_apostajb',
                'JogoDoBicho.add_apostalt',
                'JogoDoBicho.view_apostalt',
                'JogoDoBicho.view_lancejb',
                'JogoDoBicho.view_lancelt',
                'JogoDoBicho.add_apostajb'
            ])
            grupo.save()
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.usuario.username

    def idade(self):
        return date.today().year - self.data_nasc.year
    
class Bicho(models.Model):
    nome = models.CharField(max_length=60)
    grupo =  models.IntegerField(verbose_name="Grupo")
    icone = models.ImageField(upload_to='JogoDoBicho/src/img/animais', blank=True)
    dezenhas = models.CharField(max_length=11)

    def __str__(self):
        return f'{ self.nome } | Grupo: { self.grupo } | Dezenhas: { self.getDezenhas() }'

    def getDezenhas(self):
        dez = []
        for d in self.dezenhas.split('-'):
            dez.append(int(d))
        return dez

class Categoria(models.Model):
    descricao = models.CharField(max_length=30)
    valor = models.FloatField()

    def __str__(self):
        return f'{self.descricao} - R$ {self.valor}'
  
class Lance(models.Model):
    banner = models.ImageField(upload_to='JogoDoBicho/src/img/banners', blank=True, default='static/dist/img/banner.jpg')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    registro = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=14)
    fim = models.DateTimeField()
    gerente = models.ForeignKey(Administrador, on_delete=models.CASCADE, verbose_name="Administrador")      
    
    def __str__(self):
        return f'{ self.id }# LANCE - Categoria: { self.categoria.descricao }'  

    def termina(self):
        return self.estado

class Premio(models.Model):
    registro = models.DateTimeField(auto_now=True)
    posicao = models.IntegerField(verbose_name="Posição")
    resultado = models.CharField(max_length=11)
    ganhador = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Ganhador")
    valor = models.FloatField(verbose_name="Valor")

    def __str__(self):
        return f'{self.posicao} Prêmio| R$ {self.valor} p/ {self.ganhador}'

class LanceJB(Lance):
    
    premios = models.ManyToManyField(Premio, related_name="Premios")

    def get_ganhador(self, b1, b2):
        apostas = ApostaJB.objects.filter(lance__id=self.id).order_by('registro')
        for aposta in apostas:
            escolhas = aposta.escolhas.all()
            if (escolhas[0] == b1) or (escolhas[1] == b1):
                if ((escolhas[0] == b2) or (escolhas[2] == b2)) and (b1 != b2):
                    return aposta.cliente
        self.get_ganhador(self.gerar_bicho()[0], self.gerar_bicho()[1])
        
    def gerar_bicho(self):
        b1 = random.choice(Bicho.objects.all())
        while True:
            b2 = random.choice(Bicho.objects.all())
            if b1 != b2:
                return [b1, b2]

    def gerar_resultado(self):
        bichos = self.gerar_bicho()
        print(f'{bichos[0]} {bichos[1]}')
        #cont = 1
        #print(ApostaJB.objects.filter(lance__id=self.id).count())
        #for premio in self.premios.all():
            #premio = Premio.objects.create(posicao=cont, ganhador=self.get_ganhador(bichos[0], bichos[1]), valor=ApostaJB.objects.filter(lance__id=self.id).count() * self.categoria.valor)
            
        #print(self.get_ganhador(bichos[0], bichos[1]))

class Evento(models.Model):
    lance = models.ForeignKey(LanceJB, on_delete=models.DO_NOTHING, verbose_name="Lance", null=True, blank=True)
    fim = models.DateTimeField()
    

    def __str__(self) -> str:
        return f'{self.id}# Evento'

    def verificarHora(self):
        delta = (self.fim - datetime.now())
        if (delta <= timedelta(days=0, hours=0, minutes=0, seconds=0, microseconds=0)): 
            self.lance.estado = 'Encerrado'
            self.lance.gerar_resultado()
            self.lance.save()
            return True
        else:
            self.lance.estado = str(delta).split('.')[0]
            self.lance.save()
            return False
            
class LanceLT(Lance):
    pass

class Aposta(models.Model):
    registro = models.DateTimeField(auto_now=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")

class ApostaJB(Aposta):
    lance = models.ForeignKey(LanceJB, on_delete=models.CASCADE, verbose_name="Lance")
    escolhas = models.ManyToManyField(Bicho, related_name="Escolhas")
    
    def __str__(self):
        return f'Codigo: { self.id }'  

class ApostaLT(Aposta):
    lance = models.ForeignKey(LanceJB, on_delete=models.CASCADE, verbose_name="Lance")