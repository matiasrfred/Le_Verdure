# Generated by Django 4.1.1 on 2022-10-21 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calidad',
            fields=[
                ('id_calidad', models.BigIntegerField(primary_key=True, serialize=False)),
                ('descripcion_c', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'calidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CapTransporte',
            fields=[
                ('id_transporte', models.BigIntegerField(primary_key=True, serialize=False)),
                ('refrigeracion', models.IntegerField(default=False)),
                ('cap_carga', models.BigIntegerField()),
                ('cap_tamano', models.BigIntegerField()),
            ],
            options={
                'db_table': 'cap_transporte',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id_ciudad', models.BigIntegerField(primary_key=True, serialize=False)),
                ('n_ciudad', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'ciudad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id_contrato', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('contrato_activo', models.IntegerField(default=False)),
            ],
            options={
                'db_table': 'contrato',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estadisticas',
            fields=[
                ('id_estad', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'estadisticas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoPdv',
            fields=[
                ('id_estadopdv', models.BigIntegerField(primary_key=True, serialize=False)),
                ('d_estadopdv', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'estado_pdv',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('id_estado', models.BigIntegerField(primary_key=True, serialize=False)),
                ('n_estado', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'estados',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoSolicitud',
            fields=[
                ('id_estado', models.BigIntegerField(primary_key=True, serialize=False)),
                ('d_estado', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'estado_solicitud',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ofertantes',
            fields=[
                ('id_oferta', models.BigIntegerField(primary_key=True, serialize=False)),
                ('precio_oferta', models.BigIntegerField()),
                ('ctdad_ofertada', models.BigIntegerField()),
                ('seleccion', models.IntegerField(default=False)),
            ],
            options={
                'db_table': 'ofertantes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id_pais', models.BigIntegerField(primary_key=True, serialize=False)),
                ('n_pais', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'pais',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pdv',
            fields=[
                ('id_pdv', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fecha_comienzo', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('ctdad_reunida', models.BigIntegerField(blank=True, null=True)),
                ('precio_total', models.BigIntegerField(blank=True, null=True)),
                ('tipo_local', models.IntegerField(default='0')),
            ],
            options={
                'db_table': 'pdv',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_prod', models.BigIntegerField(primary_key=True, serialize=False)),
                ('n_prod', models.CharField(max_length=60)),
                ('ruta_imagen', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.BigIntegerField(primary_key=True, serialize=False)),
                ('n_rol', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'rol',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SolicitudCompra',
            fields=[
                ('id_solicitud', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fecha_solicitud', models.DateField()),
                ('ctdad_necesaria', models.BigIntegerField()),
            ],
            options={
                'db_table': 'solicitud_compra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subasta',
            fields=[
                ('id_subasta', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fecha_publicacion', models.DateField()),
                ('fecha_termino_sub', models.DateField()),
                ('cond_carga', models.BigIntegerField()),
                ('cond_tamano', models.BigIntegerField()),
                ('cond_refrigeracion', models.IntegerField(blank=True, default='0', null=True)),
                ('valor_inicial', models.BigIntegerField()),
                ('ultima_puja', models.BigIntegerField()),
                ('ctdad_pujas', models.BigIntegerField()),
                ('estado_sub', models.IntegerField(blank=True, default='0', null=True)),
            ],
            options={
                'db_table': 'subasta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id_usuario', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('run', models.BigIntegerField()),
                ('usuario_activo', models.IntegerField(default='0')),
                ('superuser', models.IntegerField(default='0')),
                ('id_ciudad', models.BigIntegerField()),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
    ]
