from django.db import models

# Create your models here.
class Estadisticas(models.Model):
    id_estad = models.BigIntegerField(primary_key=True)
    subasta_id_subasta = models.OneToOneField('Subasta', on_delete=models.DO_NOTHING, db_column='subasta_id_subasta')

    class Meta:
        managed = False
        db_table = 'estadisticas'