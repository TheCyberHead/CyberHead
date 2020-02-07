import requests
from bs4 import BeautifulSoup
from brokers.interactive_brokers.config import exchanges
from brokers.interactive_brokers.database import Scraped

def scrape_ib():
    for exchange in exchanges:
        r = requests.get('https://www.interactivebrokers.com/en/index.php?f=2222&exch={}&showcategories=STK&p=&cc=&limit=100&page=1'.format(exchange))
        data = r.text
        soup = BeautifulSoup(data, features='lxml')
        pagination = soup.find_all('ul', class_='pagination')
        last_page = int([ul.find_all('li')[-2].text for ul in pagination ][0])
        for page_num in range(1, last_page+1):
            page_request = requests.get('https://www.interactivebrokers.com/en/index.php?f=2222&exch={}&showcategories=STK&p=&cc=&limit=100&page={}'.format(exchange, page_num))
            print('Asking for page {}/{} in InteractiveBrokers.com Listings'.format(page_num, last_page))
            data = page_request.text
            soup = BeautifulSoup(data, features='lxml')
            tables = soup.find_all('table')
            table_body = tables[2].find_all('tbody')
            table_tr = table_body[0].find_all('tr')
            for tr in table_tr:
                td = tr.find_all('td')
                checkRecord = Scraped.select().where(Scraped.symbol==td[0].text)
                if not checkRecord.exists():
                    Scraped.create(
                                symbol=td[0].text,
                                exchange=exchange.upper(),
                                currency=td[3].text,
                                market='SMART',
                                symbol_type='STK'
                                )
                else:
                    print("{} already exists".format(td[0].text))


if __name__ == '__main__':
    scrape_ib()