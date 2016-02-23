# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('identificacao', models.CharField(max_length=6)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('data_alterado', models.DateTimeField(auto_now=True)),
                ('cpf', models.CharField(max_length=11)),
            ],
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='Bloco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inicio_intervalo', models.IntegerField()),
                ('fim_intervalo', models.IntegerField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('data_alterado', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('contador', models.IntegerField(default=0)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('codigo', models.IntegerField(serialize=False, primary_key=True)),
                ('descricao', models.CharField(max_length=40)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('data_alterado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('codigo', models.IntegerField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=40)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('data_alterado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConfigSinc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horas_discarte', models.IntegerField()),
                ('tempo_captura_mov', models.IntegerField()),
                ('distancia_captura_mov', models.DecimalField(max_digits=10, decimal_places=2)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('data_alterado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Configuracao_DET',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_registro', models.CharField(max_length=1)),
                ('formato', models.CharField(max_length=6)),
                ('cod_entidade', models.CharField(max_length=3)),
                ('entidade', models.CharField(max_length=40)),
                ('autuador', models.CharField(max_length=6)),
                ('tipo_arquivo', models.CharField(max_length=1)),
                ('filler', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('codigo', models.IntegerField(serialize=False, primary_key=True)),
                ('descricao', models.CharField(max_length=40)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('data_alterado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imei', models.CharField(max_length=18)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('codigo', models.IntegerField(serialize=False, primary_key=True)),
                ('descricao', models.CharField(max_length=40)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('data_alterado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Infracao',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('obs', models.TextField(null=True, blank=True)),
                ('is_estrangeiro', models.BooleanField()),
                ('is_veiculo_editado', models.BooleanField()),
                ('is_condutor_identi', models.BooleanField()),
                ('justificativa', models.TextField(null=True, blank=True)),
                ('local', models.CharField(max_length=255)),
                ('local_numero', models.CharField(max_length=100)),
                ('data_infracao', models.DateTimeField()),
                ('data_sincronizacao', models.DateTimeField(auto_now=True)),
                ('agente', models.ForeignKey(to='detransapp.Agente')),
                ('dispositivo', models.ForeignKey(to='detransapp.Dispositivo')),
            ],
        ),
        migrations.CreateModel(
            name='Infrator',
            fields=[
                ('documento', models.CharField(max_length=14, serialize=False, primary_key=True, db_index=True)),
                ('nome', models.CharField(max_length=60)),
                ('cnh', models.CharField(max_length=11, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lei',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lei', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LogImportacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_tabela', models.CharField(max_length=50)),
                ('nome_arquivo', models.CharField(max_length=50)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('data_execucao', models.DateTimeField(null=True)),
                ('data_termino', models.DateTimeField(null=True)),
                ('status', models.IntegerField(choices=[(0, b'Aguardando'), (1, b'Executando'), (2, b'Falha'), (3, b'Sucesso')])),
                ('msg_erro', models.TextField(null=True)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LogSincronizacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('solicitacao', models.IntegerField(choices=[(0, b'Download'), (1, b'Parcial'), (2, b'Recebimento infra\xc3\xa7\xc3\xa3o')])),
                ('dispositivo', models.ForeignKey(to='detransapp.Dispositivo')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MedidaAdminstrativa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=10)),
                ('descricao', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('codigo', models.IntegerField(serialize=False, primary_key=True)),
                ('descricao', models.CharField(max_length=40)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('data_alterado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tempo', models.DateTimeField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('documento', models.CharField(max_length=14, serialize=False, primary_key=True, db_index=True)),
                ('nome', models.CharField(max_length=60)),
                ('cnh', models.CharField(max_length=11, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Regiao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('data_alterado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sigla', models.CharField(max_length=150)),
                ('nome_completo', models.CharField(max_length=150)),
                ('logo', models.ImageField(upload_to=b'images/')),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoCancelamento',
            fields=[
                ('codigo', models.IntegerField(serialize=False, primary_key=True)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoInfracao',
            fields=[
                ('codigo', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('descricao', models.CharField(max_length=200)),
                ('is_condutor_obrigatorio', models.BooleanField(default=False)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('data_alterado', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('lei', models.ForeignKey(to='detransapp.Lei')),
            ],
        ),
        migrations.CreateModel(
            name='TipoVeiculo',
            fields=[
                ('codigo', models.IntegerField(serialize=False, primary_key=True)),
                ('descricao', models.CharField(max_length=40)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('data_alterado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UF',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sigla', models.CharField(max_length=2)),
                ('nome', models.CharField(max_length=50)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('data_alterado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('chassi', models.CharField(max_length=21, serialize=False, primary_key=True)),
                ('renavam', models.BigIntegerField()),
                ('nr_motor', models.CharField(max_length=21)),
                ('placa', models.CharField(max_length=7)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('data_alterado', models.DateTimeField(auto_now=True)),
                ('ano_fabricacao', models.IntegerField()),
                ('ano_modelo', models.IntegerField()),
                ('num_passageiro', models.CharField(max_length=3)),
                ('categoria', models.ForeignKey(to='detransapp.Categoria')),
                ('cidade', models.ForeignKey(to='detransapp.Cidade')),
                ('cor', models.ForeignKey(to='detransapp.Cor')),
                ('especie', models.ForeignKey(to='detransapp.Especie')),
                ('modelo', models.ForeignKey(to='detransapp.Modelo')),
                ('tipo_veiculo', models.ForeignKey(to='detransapp.TipoVeiculo')),
            ],
        ),
        migrations.CreateModel(
            name='VeiculoEditado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chassi', models.CharField(max_length=21, null=True)),
                ('renavam', models.BigIntegerField(null=True)),
                ('nr_motor', models.CharField(max_length=21, null=True)),
                ('placa', models.CharField(max_length=7)),
                ('modelo', models.CharField(max_length=40, null=True)),
                ('tipo_veiculo', models.CharField(max_length=40, null=True)),
                ('especie', models.CharField(max_length=40, null=True)),
                ('cidade', models.CharField(max_length=40, null=True)),
                ('cor', models.CharField(max_length=40, null=True)),
                ('categoria', models.CharField(max_length=40, null=True)),
                ('ano_fabricacao', models.IntegerField(null=True)),
                ('ano_modelo', models.IntegerField(null=True)),
                ('num_passageiro', models.CharField(max_length=3, null=True)),
                ('infracao', models.ForeignKey(to='detransapp.Infracao')),
                ('veiculo', models.ForeignKey(to='detransapp.Veiculo', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VeiculoEstrangeiro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pais', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('especie', models.CharField(max_length=50)),
                ('placa', models.CharField(max_length=20, null=True)),
                ('chassi', models.CharField(max_length=50, null=True)),
                ('nr_motor', models.CharField(max_length=50, null=True)),
                ('ano_fabricacao', models.IntegerField(null=True)),
                ('ano_modelo', models.IntegerField(null=True)),
                ('num_passageiro', models.CharField(max_length=3, null=True)),
                ('categoria', models.ForeignKey(to='detransapp.Categoria', null=True)),
                ('cor', models.ForeignKey(to='detransapp.Cor', null=True)),
                ('infracao', models.ForeignKey(to='detransapp.Infracao')),
                ('tipo_veiculo', models.ForeignKey(to='detransapp.TipoVeiculo', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VeiculoProprietario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('proprietario', models.ForeignKey(to='detransapp.Proprietario')),
                ('veiculo', models.ForeignKey(to='detransapp.Veiculo')),
            ],
        ),
        migrations.AddField(
            model_name='infracao',
            name='infrator',
            field=models.ForeignKey(to='detransapp.Infrator', null=True),
        ),
        migrations.AddField(
            model_name='infracao',
            name='movimento',
            field=models.ForeignKey(to='detransapp.Movimentacao', null=True),
        ),
        migrations.AddField(
            model_name='infracao',
            name='tipo_cancelamento',
            field=models.ForeignKey(blank=True, to='detransapp.TipoCancelamento', null=True),
        ),
        migrations.AddField(
            model_name='infracao',
            name='tipo_infracao',
            field=models.ForeignKey(to='detransapp.TipoInfracao'),
        ),
        migrations.AddField(
            model_name='infracao',
            name='veiculo',
            field=models.ForeignKey(to='detransapp.Veiculo', null=True),
        ),
        migrations.AddField(
            model_name='cidade',
            name='uf',
            field=models.ForeignKey(to='detransapp.UF'),
        ),
        migrations.AddField(
            model_name='agente',
            name='movimentos',
            field=models.ManyToManyField(to='detransapp.Movimentacao'),
        ),
        migrations.AddField(
            model_name='agente',
            name='regioes',
            field=models.ManyToManyField(to='detransapp.Regiao'),
        ),
    ]
