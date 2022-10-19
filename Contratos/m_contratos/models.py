from django.db import models

# Create your models here.

class Contrato(models.Model):
    id_contrato = models.BigIntegerField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    contrato_activo = models.BooleanField(default = False)
    usuario_id_usuario = models.OneToOneField('Usuario', on_delete=models.DO_NOTHING, db_column='usuario_id_usuario')

    class Meta:
        managed = False
        db_table = 'contrato'

class Rol(models.Model):
    id_rol = models.BigIntegerField(primary_key=True)
    n_rol = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rol'

class Usuario(models.Model):
    id_usuario = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    run = models.BigIntegerField()
    usuario_activo = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)
    ciudad_id_ciudad = models.ForeignKey(Ciudad, on_delete=models.DO_NOTHING, db_column='ciudad_id_ciudad')
    rol_id_rol = models.ForeignKey(Rol, on_delete=models.DO_NOTHING, db_column='rol_id_rol')
    id_ciudad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'usuario'
