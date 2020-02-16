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
	description = peewee.CharField()
	source = peewee.CharField()
	class Meta:
	    database = db
	    db_table = 'dataset'

class History(peewee.Model):
	dataset_id = peewee.ForeignKeyField(DataSet)
	datetime = peewee.DateTimeField()
	bid = peewee.FloatField()
	ask = peewee.FloatField()
	class Meta:
	    database = db
	    db_table = 'history'


if __name__ == '__main__':
	if not DataSet.table_exists():
		DataSet.create_table()
		print('Data Sets table created.')
	if not History.table_exists():
		History.create_table()
		print('History table created.')