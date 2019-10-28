from ib.ext.Contract import Contract

def makeContract(ticker):
    contract = Contract()
    contract.m_symbol = ticker
    contract.m_secType = 'STK'
    contract.m_exchange = 'SMART'
    contract.m_currency = 'USD'
    print(contract)
    return contract


def makeStkContract(contractTuple):
    newContract = Contract()
    newContract.m_symbol = contractTuple[0]
    newContract.m_secType = contractTuple[1]
    newContract.m_exchange = contractTuple[2]
    newContract.m_currency = contractTuple[3]
    newContract.m_expiry = contractTuple[4]
    newContract.m_strike = contractTuple[5]
    newContract.m_right = contractTuple[6]
    print('Contract Values:%s,%s,%s,%s,%s,%s,%s:' % contractTuple)
    return newContract