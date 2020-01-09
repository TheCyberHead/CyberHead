import cyberhead as ch
import random

broker = ch.brokers.interactive
random_trade = random.choice([True, False])

if random_trade:
  broker.buy('1000', 'TSLA')
