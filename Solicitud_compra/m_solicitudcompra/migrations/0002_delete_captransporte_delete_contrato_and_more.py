# Generated by Django 4.1.1 on 2022-11-30 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('m_solicitudcompra', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CapTransporte',
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
            name='Ofertantes',
        ),
        migrations.DeleteModel(
            name='Pdv',
        ),
        migrations.DeleteModel(
            name='Subasta',
        ),
    ]