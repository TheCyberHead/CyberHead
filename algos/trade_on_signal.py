import cyberhead as ch
from time import sleep

signal = ch.databases.redis.signals.position
broker = ch.brokers.interactive

while True:
  if signal[-1] == 'Long':
    broker.buy('1000', 'TSLA')
  if signal[-1] == 'Short':
    broker.sell('1000', 'TSLA')
  sleep(1000)
