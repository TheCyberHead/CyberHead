from sqlalchemy import create_engine
import peewee
import os


user = os.getenv('CH_DB_USER')
password = os.getenv('CH_DB_PASSWORD')
host = os.getenv('CH_DB_HOST')
name = os.getenv('CH_DB_NAME')

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{name}")
engine.connect()


if __name__ == '__main__':
	modules = filter(lambda x: x != '__init__.py', os.listdir("modules"))
	for module in modules:
		try:
			os.listdir(f"modules/{module}").index('db.py')
			exec(f"from modules.{module}.db import *")
		except Exception as e:
			print(f'Database file not found in module {module}')
	try:
		print('--------')
		databases = list(globals())
		split_db = databases[databases.index('db')+1:]
		for database in split_db:
			exec(f"{database}.create_table()")
			print(database)
	except Exception as e:
		print(f"Database Integration Error. {e}")
