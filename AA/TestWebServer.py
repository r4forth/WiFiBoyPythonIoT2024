from machine import Pin
import network
import socket
import time
import wifi

# 定義內建 LED 與 LCD 背光腳位
LED = Pin(16, Pin.OUT)
SCREEN = Pin(27, Pin.OUT)

# 設定初始值
LED.value(1)  # OFF
SCREEN.value(0)  # OFF

LED_state = "內建 LED 目前是關閉狀態"
SCREEN_state = "螢幕背光 目前是關閉狀態"

# 設定 WiFi 連線參數
SSID = 'DoraHome300M'
PASSWORD = '0975393503@'

wlan = network.WLAN(network.STA_IF)

# 連接 WiFi
station = wifi.connect(SSID, PASSWORD)

#HTML + CSS for webpage
html = """<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>玩學機網頁控制程式</title>
  <style>
    html {
      font-family: Arial;
      display: inline-block;
      margin: 0px auto;
      text-align: center;
    }
    
    h1 {
      font-family: Arial;
      color: #2551cc;
    }
    
    .button1,
    .button2 {
      -webkit-border-radius: 10;
      -moz-border-radius: 10;
      border-radius: 10px;
      font-family: Arial;
      color: #ffffff;
      font-size: 30px;
      padding: 10px 20px 10px 20px;
      text-decoration: none;
      display: inline-block;
      margin: 5px;
    }
    
    .button1 {
      background: #339966;
    }
    
    .button2 {
      background: #000000;
    }
  </style>
</head>

<body>
  <h1>玩學機網頁控制程式</h1>
  <p>%s</p>
  <p>
    <a href="/LED/on"><button class="button1">內建 LED 開啟</button></a>
    <a href="/LED/off"><button class="button2">內建 LED 關閉</button></a>
  </p>
  <p>%s</p>
  <p>
    <a href="/SCREEN/on"><button class="button1">LCD 螢幕背光 開啟</button></a>
    <a href="/SCREEN/off"><button class="button2">LCD 螢幕背光 關閉</button></a>
  </p>
</body>
</html>
"""

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setblocking(0)
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    if wlan.isconnected():
        try:
            cl, addr = s.accept()
            print('client connected from', addr)
            request = cl.recv(1024)
            print(request)

            request = str(request)
            # 判斷請求中的特定指令
            LED_on = '/LED/on' in request
            LED_off = '/LED/off' in request
            SCREEN_on = '/SCREEN/on' in request
            SCREEN_off = '/SCREEN/off' in request
            # 控制 LED
            if LED_on:
                print("內建 LED 開啟")
                LED.value(0)
                LED_state = "內建 LED 開啟"
            if LED_off:
                print("內建 LED 關閉")
                LED.value(1)
                LED_state = "內建 LED 關閉"
            if SCREEN_on:
                print("LCD 螢幕背光 開啟")
                SCREEN.value(1)
                SCREEN_state = "LCD 螢幕背光 開啟"
            if SCREEN_off:
                print("LCD 螢幕背光 關閉")
                SCREEN.value(0)
                SCREEN_state = "LCD 螢幕背光 關閉"
                
            response = html % (LED_state, SCREEN_state)
            cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
            cl.send(response)
            cl.close()

        except:
            pass
    time.sleep(0.1)