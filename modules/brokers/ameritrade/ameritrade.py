import requests
import json

def get_account_details(token):
	headers = {
		"Authorization": f"Bearer {token}",
	}
	req = requests.get('https://api.tdameritrade.com/v1/accounts', headers=headers)
	return req.json()


def place_order_tda(action, quantity, ticker, account_id, bearer):
	headers = {
		'Authorization': 'Bearer {}'.format(bearer)
	}
	payload = {
	  "orderType": "MARKET",
	  "session": "NORMAL",
	  "duration": "DAY",
	  "orderStrategyType": "SINGLE",
	  "orderLegCollection": [
	    {
	      "instruction": action,
	      "quantity": quantity,
	      "instrument": {
	        "symbol": ticker,
	        "assetType": "EQUITY"
	      }
	    }
	  ]
	}
	url = 'https://api.tdameritrade.com/v1/accounts/{}/orders'.format(account_id)	
	req = requests.post(url, headers=headers, json=payload)
	return req.status_code

def place_limit_order_tda(action, entry_price, exit_price, ticker, quantity, order_type, bearer, account_id):
	headers = {
		'Authorization': 'Bearer {}'.format(bearer)
	}
	exit_action = "Sell" if action == 'Buy' else "Buy"
	payload = {
	  "orderType": "LIMIT",
	  "session": "NORMAL",
	  "price": entry_price,
	  "duration": order_type,
	  "orderStrategyType": "TRIGGER",
	  "orderLegCollection": [
	    {
	      "instruction": action,
	      "quantity": quantity,
	      "instrument": {
	        "symbol": ticker,
	        "assetType": "EQUITY"
	      }
	    }
	  ],
	  "childOrderStrategies": [
	    {
	      "orderType": "LIMIT",
	      "session": "NORMAL",
	      "price": exit_price,
	      "duration": order_type,
	      "orderStrategyType": "SINGLE",
	      "orderLegCollection": [
	        {
	          "instruction": exit_action,
	          "quantity": quantity,
	          "instrument": {
	            "symbol": ticker,
	            "assetType": "EQUITY"
	          }
	        }
	      ]
	    }
	  ]
	}
	url = 'https://api.tdameritrade.com/v1/accounts/{}/orders'.format(account_id)
	req = requests.post(url, headers=headers, json=payload)
	return req.status_code
