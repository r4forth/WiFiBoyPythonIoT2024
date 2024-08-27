 # CWA-D1DA3647-D49E-4EEF-B9ED-0814E6CE849F
import network
import ntptime
import wifi
import urequests
import ujson
from machine import Pin, I2C, RTC
import time

# 設定 WiFi 連線參數
SSID = 'DoraHome300M'
PASSWORD = '0975393503@'


def sync_time():
    ntptime.settime()  # 使用 NTP 伺服器同步時間

def get_weather_data():
    url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWA-D1DA3647-D49E-4EEF-B9ED-0814E6CE849F&format=JSON&locationName=%E6%A1%83%E5%9C%92%E5%B8%82'
    response = urequests.get(url)
    data = ujson.loads(response.text)
    # print(data)
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
    return result

# def showWeather():
#     # result = [location, startTime, endTime, weather_state, rain_prob, min_tem, comfort, max_tem]
#     max_temp = get_weather_data()[7]
#     min_temp = get_weather_data()[5]
#     weather_state = get_weather_data()[3]
#     return 

def display_time_and_weather():
    rtc = RTC()
    result = get_weather_data()
    max_temp = result[7]
    min_temp = result[5]
    weather_state = result[3]
    # 顯示氣溫與風向
    wb.str(f'Max Temp: {max_temp}°C', 0, 20)
    wb.str(f'Min Temp: {min_temp}°C', 0, 40)
    wb.str(f'weather_state: {weather_state}', 0, 60)
#     while True:
#         # 顯示年月日 時分秒
#         current_time = rtc.datetime()
#         year = current_time[0]
#         month = current_time[1]
#         day = current_time[2]
#         hour = current_time[4] + 8
#         minute = current_time[5]
#         second = current_time[6]
#         
#         wb.cls()
#         wb.str(f'{year}/{month}/{day} {hour}:{minute}:{second}', 10, 20)
#         # showWeather()
#         if hour == 0 and minute == 0 and second == 0:  # 每小時更新一次
#             showWeather()
#             # 顯示圖像
#             wb.showbmp('/path/to/temperature_icon.bmp', 80, 20)
#             wb.showbmp('/path/to/wind_direction_icon.bmp', 80, 40)
#         time.sleep(1)

# 主程式流程
def main():
    # 網路連線
    station = wifi.connect(SSID, PASSWORD)
    sync_time()
    display_time_and_weather()

if __name__ == '__main__':
    main()
