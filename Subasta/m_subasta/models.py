from django.db import models

# Create your models here.

class Subasta(models.Model):
    id_subasta = models.BigIntegerField(primary_key=True)
    fecha_publicacion = models.DateField()
    fecha_termino_sub = models.DateField()
    cond_carga = models.BigIntegerField()
    cond_tamano = models.BigIntegerField()
    cond_refrigeracion = models.BooleanField(default=False,blank=True, null=True)
    valor_inicial = models.BigIntegerField()
    ultima_puja = models.BigIntegerField()
    ctdad_pujas = models.BigIntegerField()
    pdv_id_pdv = models.ForeignKey('Pdv', on_delete=models.DO_NOTHING, db_column='pdv_id_pdv')
    estado_sub = models.BooleanField(default=False,blank=True, null=True)
    cap_transporte_id_transporte = models.ForeignKey('CapTransporte', on_delete=models.DO_NOTHING, db_column='cap_transporte_id_transporte')

    class Meta:
        managed = False
        db_table = 'subasta'

