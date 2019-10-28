from datetime import datetime
from time import sleep
from brokers.interactive_brokers import scraper
from brokers.interactive_brokers import historical_collector
from brokers.interactive_brokers import fundamental_collector
from brokers.interactive_brokers import client_persistence

if __name__=='__main__':
    print('[{}] SCRAPER INITIALIZED'
          ''.format(datetime.now().replace(microsecond=0)))
    scraper.scrap()
    print('[{}] scraper terminated\n'
          ''.format(datetime.now().replace(microsecond=0)))
    print('[{}] HISTORICAL COLLECTOR INITIALIZED'
          ''.format(datetime.now().replace(microsecond=0)))
    historical_collector.recurrent_action()
    print('[{}] historical collector terminated\n'
          ''.format(datetime.now().replace(microsecond=0)))
    print('[{}] FUNDAMENTAL COLLECTOR INITIALIZED'
          ''.format(datetime.now().replace(microsecond=0)))
    fundamental_collector.recurrent_action()
    print('[{}] funtamental collector terminated'
          ''.format(datetime.now().replace(microsecond=0)))

