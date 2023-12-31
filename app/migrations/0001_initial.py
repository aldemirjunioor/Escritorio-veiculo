# Generated by Django 5.0 on 2023-12-05 03:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoVeiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nome_veiculo', models.CharField(max_length=90)),
                ('ar_cond', models.CharField(choices=[('sim', 'Sim'), ('não', 'Não')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_hab', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Número da Habilitação')),
                ('stado_hab', models.CharField(choices=[('vencida', 'Vencida'), ('válida', 'Válida')], max_length=7, verbose_name='Estado da Habilitação')),
                ('nome_cliente', models.CharField(max_length=150, verbose_name='Nome do Cliente')),
                ('end_cliente', models.CharField(max_length=200, verbose_name='Endereço do Cliente')),
                ('tel_cliente', models.CharField(max_length=15, verbose_name='Telefone do Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.DecimalField(decimal_places=0, max_digits=8, verbose_name='Numero do Contrato')),
                ('num_escritorio', models.DecimalField(decimal_places=0, max_digits=8, verbose_name='Numero do Escritório')),
                ('data', models.DateField(verbose_name='Data do Contrato')),
                ('duracao', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Duração do Contrato')),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_veiculo', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Número do Veículo')),
                ('data_prox_manut', models.DateField(verbose_name='Data da Próxima Manutenção')),
                ('placa', models.CharField(max_length=10, verbose_name='Número do Placa')),
            ],
        ),
        migrations.CreateModel(
            name='Automovel',
            fields=[
                ('tipoveiculo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.tipoveiculo')),
                ('num_portas', models.DecimalField(decimal_places=0, max_digits=2)),
                ('dir_hidraulica', models.CharField(choices=[('sim', 'Sim'), ('não', 'Não')], max_length=3)),
                ('cambio_auto', models.CharField(choices=[('sim', 'Sim'), ('não', 'Não')], max_length=3)),
            ],
            bases=('app.tipoveiculo',),
        ),
        migrations.CreateModel(
            name='Onibus',
            fields=[
                ('tipoveiculo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.tipoveiculo')),
                ('num_passag', models.DecimalField(decimal_places=0, max_digits=3)),
                ('leito', models.CharField(max_length=30)),
                ('sanitario', models.CharField(choices=[('sim', 'Sim'), ('não', 'Não')], max_length=3)),
            ],
            bases=('app.tipoveiculo',),
        ),
        migrations.CreateModel(
            name='Escritorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(max_length=150)),
                ('num_contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.contrato')),
            ],
        ),
    ]
