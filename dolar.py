import requests
import json


dolar_blue = 'https://api-dolar-argentina.herokuapp.com/api/dolarblue'
dolar_oficial = 'https://api-dolar-argentina.herokuapp.com/api/dolaroficial'




async def getValueUsd():
	valor_db = requests.get(dolar_blue).json()
	#valor_do = requests.get(dolar_oficial).json()
	return valor_db['venta']
	#print(valor_do['venta'])


