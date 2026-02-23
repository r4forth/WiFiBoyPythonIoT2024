import urequests
import wb_config
import json   
url='https://steam.oxxostudio.tw/download/python/json-demo.json'
response=urequests.get(url)
#ubike=json.loads(response.text)
#print(ubike[0])