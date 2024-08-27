import urequests
import wifi
import ujson
# 設定 WiFi 連線參數
SSID = 'DoraHome300M'
PASSWORD = '0975393503@'
station = wifi.connect(SSID, PASSWORD)
# 中央氣象局查詢
url='https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWA-D1DA3647-D49E-4EEF-B9ED-0814E6CE849F&format=JSON&locationName=%E6%A1%83%E5%9C%92%E5%B8%82'

response = urequests.get(url)
data = ujson.loads(response.text)
# print(response.status_code)


location = data["records"]["location"][0]["locationName"]
weatherElements = data["records"]["location"][0]["weatherElement"]
startTime = weatherElements[0]["time"][0]["startTime"]
endTime = weatherElements[0]["time"][0]["endTime"]
weather_state = weatherElements[0]["time"][0]["parameter"]["parameterName"]
rain_prob = weatherElements[1]["time"][0]["parameter"]["parameterName"]
min_tem = weatherElements[2]["time"][0]["parameter"]["parameterName"]
comfort = weatherElements[3]["time"][0]["parameter"]["parameterName"]
max_tem = weatherElements[4]["time"][0]["parameter"]["parameterName"]

result = [location, startTime, endTime, weather_state, rain_prob, min_tem, comfort, max_tem]
print(startTime)

for i in result:
    print(i)
wb.cls()
wb.str('Taoyuan', 10, 20, 2, 2)
wb.str('Min Temp: ' + result[5], 10, 40, 2, 2)
wb.str('Max Temp: ' + result[7], 10, 80, 2, 2)
wb.str('Rain %: ' + result[4] + ' %', 10, 100, 2, 2)


