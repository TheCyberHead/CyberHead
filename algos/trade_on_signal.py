import cyberhead as ch

signal = ch.databases.redis.signals.position
broker = ch.brokers.interactive

if signal[-1] == 'Long':
  broker.buy()
