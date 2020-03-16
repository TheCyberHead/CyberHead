from datetime import now, detaatime

from cyberhead import mysql, alpaca

CALL_BACK_TIME = 100  #seconds

broker = alpaca
last_signal = mysql.signal[-1]

new_signal = last_signal.time > now() - ten_seconds

if new_signal and last_sinal.buy:
    broker.buy()
