from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import datetime
import backtrader as bt


class TestStrategy(bt.Strategy):
	def log(self, txt, dt=None):
		dt = dt or self.datas[0].datetime.date(0)
		print('%s, %s' % (dt.isoformat(), txt))

	def __init__(self):
		self.dataclose = self.datas[0].close

	def notify_order(self, order):
		if order.status in [order.Completed]:
			if order.isbuy():
				self.log(
                    'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))

				self.buyprice = order.executed.price
				self.buycomm = order.executed.comm
			else: 
				self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))

			self.bar_executed = len(self)

		elif order.status in [order.Canceled, order.Margin, order.Rejected]:
			self.log('Order Canceled/Margin/Rejected')

		self.order = None

	def next(self):
		if not self.position:
			if self.dataclose[0] < self.dataclose[-1]:
				diff = 1-(self.dataclose[-1]/self.dataclose[0])
				if diff <= -0.10:
					self.log('BUY CREATE, %.2f' % self.dataclose[0])
					self.order = self.buy(size=300)
		else:
			self.log('SELL CREATE, %.2f' % self.dataclose[0])
			self.order = self.sell(size=300)


if __name__ == '__main__':
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(100000.0)
    cerebro.addstrategy(TestStrategy)
    data = bt.feeds.YahooFinanceCSVData(
        dataname='FB.csv',
        fromdate=datetime.datetime(2018, 12, 14),
        todate=datetime.datetime(2019, 10, 7),
        reverse=False)
    cerebro.adddata(data)
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
