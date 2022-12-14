# Generated by Django 4.1.3 on 2022-11-02 08:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Concourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('draw_date', models.DateTimeField()),
                ('result', models.CharField(blank=True, max_length=100)),
                ('collection', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed'), ('Encerrado', 'Encerrado')], default='Open', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, default='', upload_to='MegaSena/profile_photos/')),
                ('gender', models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Não Declarar', 'Não Declarar')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity_numbers', models.IntegerField()),
                ('teimosinha', models.IntegerField()),
                ('bet_type', models.CharField(choices=[('Simples', 'Simples'), ('Bolão', 'Bolão')], default='Simples', max_length=10)),
                ('numbers', models.CharField(default='[]', max_length=100)),
                ('concourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MegaSena.concourse')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bank_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('saldo', models.FloatField(max_length=100)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MegaSena.profile')),
            ],
        ),
    ]
