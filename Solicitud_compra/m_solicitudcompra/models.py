from django.db import models

# Create your models here.

class Calidad(models.Model):
    id_calidad = models.BigIntegerField(primary_key=True)
    descripcion_c = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'calidad'

class Producto(models.Model):
    id_prod = models.BigIntegerField(primary_key=True)
    n_prod = models.CharField(max_length=60)
    ruta_imagen = models.CharField(max_length=200)
    calidad_id_calidad = models.ForeignKey(Calidad, on_delete=models.DO_NOTHING, db_column='calidad_id_calidad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'

class EstadoSolicitud(models.Model):
    id_estado = models.BigIntegerField(primary_key=True)
    d_estado = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estado_solicitud'

class SolicitudCompra(models.Model):
    id_solicitud = models.BigIntegerField(primary_key=True)
    fecha_solicitud = models.DateField()
    ctdad_necesaria = models.BigIntegerField()
    estado_solicitud_id_estado = models.ForeignKey(EstadoSolicitud, on_delete=models.DO_NOTHING, db_column='estado_solicitud_id_estado')
    producto_id_prod = models.ForeignKey(Producto, on_delete=models.DO_NOTHING, db_column='producto_id_prod')
    usuario_id_usuario = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING, db_column='usuario_id_usuario')

    class Meta:
        managed = False
        db_table = 'solicitud_compra'
