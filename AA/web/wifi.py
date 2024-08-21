import network

def connect(ssid, password):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    
    while not station.isconnected():
        pass

    print('WiFi 連接成功')
    print('IP 設定:', station.ifconfig())
    return station