import requests
import json


url_btc = "https://bitpay.com/api/rates"

async def getValueBTCtoUSD():
	value_btc = requests.get(url_btc).json()
	value_btc_usd = value_btc[2]["rate"]
	return value_btc_usd

	
