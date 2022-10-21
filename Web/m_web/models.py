from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Pais(models.Model):
    id_pais = models.BigIntegerField(primary_key=True)
    n_pais = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'pais'

class Estados(models.Model):
    id_estado = models.BigIntegerField(primary_key=True)
    n_estado = models.CharField(max_length=100)
    pais_id_pais = models.ForeignKey('Pais', on_delete=models.DO_NOTHING, db_column='pais_id_pais', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados'

class Ciudad(models.Model):
    id_ciudad = models.BigIntegerField(primary_key=True)
    n_ciudad = models.CharField(max_length=50)
    estados_id_estado = models.ForeignKey('Estados', on_delete=models.DO_NOTHING, db_column='estados_id_estado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ciudad'

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
    calidad_id_calidad = models.ForeignKey('Calidad', on_delete=models.DO_NOTHING, db_column='calidad_id_calidad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class Rol(models.Model):
    id_rol = models.BigIntegerField(primary_key=True)
    n_rol = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rol'

class Usuario(AbstractBaseUser):
    id_usuario = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    run = models.BigIntegerField()
    usuario_activo = models.IntegerField(default='0')
    superuser = models.IntegerField(default='0')
    ciudad_id_ciudad = models.ForeignKey('Ciudad', on_delete=models.DO_NOTHING, db_column='ciudad_id_ciudad')
    rol_id_rol = models.ForeignKey('Rol', on_delete=models.DO_NOTHING, db_column='rol_id_rol')
    id_ciudad = models.BigIntegerField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre','apellido','password','run']

    class Meta:
        managed = False
        db_table = 'usuario'

class Contrato(models.Model):
    id_contrato = models.BigIntegerField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    contrato_activo = models.IntegerField(default = False)
    usuario_id_usuario = models.OneToOneField('Usuario', on_delete=models.DO_NOTHING, db_column='usuario_id_usuario')

    class Meta:
        managed = False
        db_table = 'contrato'

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
    estado_solicitud_id_estado = models.ForeignKey('EstadoSolicitud', on_delete=models.DO_NOTHING, db_column='estado_solicitud_id_estado')
    producto_id_prod = models.ForeignKey('Producto', on_delete=models.DO_NOTHING, db_column='producto_id_prod')
    usuario_id_usuario = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING, db_column='usuario_id_usuario')

    class Meta:
        managed = False
        db_table = 'solicitud_compra'

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
    estado_pdv_id_estadopdv = models.ForeignKey('EstadoPdv', on_delete=models.DO_NOTHING, db_column='estado_pdv_id_estadopdv')
    solicitud_compra_id_solicitud = models.OneToOneField('SolicitudCompra', on_delete=models.DO_NOTHING, db_column='solicitud_compra_id_solicitud')
    tipo_local = models.IntegerField(default='0')

    class Meta:
        managed = False
        db_table = 'pdv'

class Ofertantes(models.Model):
    id_oferta = models.BigIntegerField(primary_key=True)
    precio_oferta = models.BigIntegerField()
    ctdad_ofertada = models.BigIntegerField()
    seleccion = models.IntegerField(default = False)
    pdv_id_pdv = models.ForeignKey('Pdv', on_delete=models.DO_NOTHING, db_column='pdv_id_pdv', blank=True, null=True)
    usuario_id_usuario = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING, db_column='usuario_id_usuario')

    class Meta:
        managed = False
        db_table = 'ofertantes'

class CapTransporte(models.Model):
    id_transporte = models.BigIntegerField(primary_key=True)
    refrigeracion = models.IntegerField(default = False, null=False)
    cap_carga = models.BigIntegerField()
    cap_tamano = models.BigIntegerField()
    usuario_id_usuario = models.OneToOneField('Usuario', on_delete=models.DO_NOTHING, db_column='usuario_id_usuario')

    class Meta:
        managed = False
        db_table = 'cap_transporte'



class Subasta(models.Model):
    id_subasta = models.BigIntegerField(primary_key=True)
    fecha_publicacion = models.DateField()
    fecha_termino_sub = models.DateField()
    cond_carga = models.BigIntegerField()
    cond_tamano = models.BigIntegerField()
    cond_refrigeracion = models.IntegerField(default='0',blank=True, null=True)
    valor_inicial = models.BigIntegerField()
    ultima_puja = models.BigIntegerField()
    ctdad_pujas = models.BigIntegerField()
    pdv_id_pdv = models.ForeignKey('Pdv', on_delete=models.DO_NOTHING, db_column='pdv_id_pdv')
    estado_sub = models.IntegerField(default='0',blank=True, null=True)
    cap_transporte_id_transporte = models.ForeignKey('CapTransporte', on_delete=models.DO_NOTHING, db_column='cap_transporte_id_transporte')

    class Meta:
        managed = False
        db_table = 'subasta'

class Estadisticas(models.Model):
    id_estad = models.BigIntegerField(primary_key=True)
    subasta_id_subasta = models.OneToOneField('Subasta', on_delete=models.DO_NOTHING, db_column='subasta_id_subasta')

    class Meta:
        managed = False
        db_table = 'estadisticas'