# Generated by Django 4.1.1 on 2022-10-23 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('m_usuario', '0002_calidad_contrato_estadisticas_estadopdv_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Calidad',
        ),
        migrations.DeleteModel(
            name='Contrato',
        ),
        migrations.DeleteModel(
            name='Estadisticas',
        ),
        migrations.DeleteModel(
            name='EstadoPdv',
        ),
        migrations.DeleteModel(
            name='EstadoSolicitud',
        ),
        migrations.DeleteModel(
            name='Ofertantes',
        ),
        migrations.DeleteModel(
            name='Pdv',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.DeleteModel(
            name='SolicitudCompra',
        ),
        migrations.DeleteModel(
            name='Subasta',
        ),
    ]
