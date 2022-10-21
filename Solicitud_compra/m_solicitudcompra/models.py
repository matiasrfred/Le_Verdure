# Create your models here.

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