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


