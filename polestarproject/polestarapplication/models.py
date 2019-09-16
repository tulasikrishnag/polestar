from django.db import models

from datetime import datetime 
from django.utils import timezone
from datetime import timedelta 
from django.utils.timezone import make_aware
  # Create your models here.
class ShipPositionDetails(models.Model):
	imo = models.BigIntegerField()
	position_dt_tm = models.DateTimeField()
	latitude= models.DecimalField(max_digits=10,decimal_places=8)
	longitude= models.DecimalField(max_digits=11,decimal_places=8)
	created_date= models.DateTimeField(default=make_aware(datetime.now()))
	class Meta:
		constraints = [
            models.UniqueConstraint(fields=['imo', 'position_dt_tm'], name='imo_position_dt_uniq')
        ]
		db_table ="ship_position_details"


class ShipDetail(models.Model):
	imo = models.BigIntegerField()
	name = models.CharField(max_length=30)
	class Meta:
		constraints = [
            models.UniqueConstraint(fields=['imo', 'name'], name='ship_name_uniq')
        ]
		db_table ="ship_detail"