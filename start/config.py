from django.contrib.auth.models import User, Group
from JogoDoBicho.models import Administrador, Bicho, Categoria

admin_grupo = Group.objects.create(name='Administradores')
admin_grupo.save()

cliente_grupo = Group.objects.create(name='Clientes')
cliente_grupo.save()

admin_user = User.objects.all()[0]
admin_user.first_name = 'Administrador'
admin_user.last_name = 'Geral'
admin_user.groups.add(Group.objects.get(name='Administradores'))
admin_user.save()
admin_model = Administrador.objects.create(usuario=admin_user, cpf='000.000.000-00', data_nasc='2000-01-01')
