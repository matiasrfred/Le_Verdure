from django.db import models

# Create your models here.

class EstadoPdv(models.Model):
    id_estadopdv = models.BigIntegerField(primary_key=True)
    d_estadopdv = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'estado_pdv'

class Pdv(models.Model):
    id_pdv = models.BigIntegerField(primary_key=True)
    fecha_comienzo = models.DateField()
    fecha_termino = models.DateField()
    ctdad_reunida = models.BigIntegerField(blank=True, null=True)
    precio_total = models.BigIntegerField(blank=True, null=True)
    estado_pdv_id_estadopdv = models.ForeignKey(EstadoPdv, on_delete=models.DO_NOTHING, db_column='estado_pdv_id_estadopdv')
    solicitud_compra_id_solicitud = models.OneToOneField('SolicitudCompra', on_delete=models.DO_NOTHING, db_column='solicitud_compra_id_solicitud')
    tipo_local = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'pdv'

class Ofertantes(models.Model):
    id_oferta = models.BigIntegerField(primary_key=True)
    precio_oferta = models.BigIntegerField()
    ctdad_ofertada = models.BigIntegerField()
    seleccion = models.BooleanField(default = False)
    pdv_id_pdv = models.ForeignKey(Pdv, on_delete=models.DO_NOTHING, db_column='pdv_id_pdv', blank=True, null=True)
    usuario_id_usuario = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING, db_column='usuario_id_usuario')

    class Meta:
        managed = False
        db_table = 'ofertantes'
