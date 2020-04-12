import peewee
import os

db = peewee.MySQLDatabase(os.getenv('CH_DB_NAME'),
                          host=os.getenv('CH_DB_HOST'),
                          port=3306,
                          user=os.getenv('CH_DB_USER'),
                          password=os.getenv('CH_DB_PASSWORD'))


class DataSet(peewee.Model):
	identifier = peewee.CharField()
	reference_symbol = peewee.CharField()
	symbol = peewee.CharField()
	source = peewee.CharField()
	frecuency = peewee.CharField()
	first_fetch = peewee.BooleanField(default=False)
	class Meta:
	    database = db
	    db_table = 'dataset'

class History(peewee.Model):
	dataset_id = peewee.ForeignKeyField(DataSet)
	datetime = peewee.DateTimeField()
	open_price = peewee.FloatField()
	high_price = peewee.FloatField()
	low_price = peewee.FloatField()
	closing_price = peewee.FloatField()
	volume = peewee.IntegerField()
	class Meta:
	    database = db
	    db_table = 'history'