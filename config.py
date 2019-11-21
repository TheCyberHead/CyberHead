exchanges = ['NYSE']
# Exchanges : NYSE, TSX, NASDAQ, etc.
historical_from = '1 Y' 
# Historical : 1 X, X : Y - M - D 
bar_length = '1 day'
# Length : X minutes / hours / seconds days
ib_host = "127.0.0.1"
# TWS API IP Host
ib_port = 7496
# TWS API IP Port
ib_client_id = 100
# TWS API Client ID
db_host = 'localhost'
db_user = 'root'
db_password = 'root'
db_name = 'collector'
db_port = 3306
drops = -0.12
recover = 0.03