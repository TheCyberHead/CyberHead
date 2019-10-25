from ib.ext.Order import Order
from ib.opt import ibConnection
from interactive import makeContract
from time import sleep

def watcher(msg):
	print(msg)

def create_order(order_type, quantity, action, orderRef):
	order = Order()
	order.m_action = action
	order.m_orderType = order_type
	order.m_totalQuantity = quantity
	order.m_orderRef = orderRef
	return order


def execute_order(order_id, contract, order):
	con = ibConnection(port=7496, clientId=100)
	con.registerAll(watcher)
	con.connect()
	con.placeOrder(order_id, contract, order)
	sleep(10)
	con.disconnect()


if __name__ == '__main__':
	execute_order(112323, makeContract('AAPL'), create_order('MKT', 100, 'SELL', 'POR FAVOR FUNCIONA'))