import cyberhead as ch
import random
from time import sleep

broker = ch.brokers.interactive
random_trade = random.choice([True, False])

while True:
  if random_trade:
    broker.buy('1000', 'TSLA')
  sleep(1000000)
