# 簡單WebServer 程式
import socket
import wifi

# 設定 WiFi 連線參數
SSID = 'DoraHome300M'
PASSWORD = '0975393503@'

# 連接 WiFi
station = wifi.connect(SSID, PASSWORD)

# 其他主程式邏輯
# 例如：啟動網頁伺服器或其他應用
# 讀取 index.html 檔案的內容
def read_html_file():
    try:
        with open('index.html', 'r') as file:
            return file.read()
    except Exception as e:
        print("無法讀取 index.html 檔案:", e)
        return "<h1>500 Internal Server Error</h1>"

# 建立套接字
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('伺服器啟動，等待連接...')

while True:
    cl, addr = s.accept()
    print('客戶端連接來自', addr)
    
    # 接收 HTTP 請求
    request = cl.recv(1024)
    print('請求內容:', request)
    
    # 讀取並發送 index.html 檔案的內容
    response = read_html_file()
    
    cl.send('HTTP/1.1 200 OK\r\n')
    cl.send('Content-Type: text/html\r\n')
    cl.send('Connection: close\r\n\r\n')
    cl.sendall(response)
    
    # 關閉連接
    cl.close()