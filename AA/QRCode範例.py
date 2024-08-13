from lib.uQR import QRCode

wb.cls()

qr = QRCode()
# qr.add_data('https://www.wifiboy.org')
qr.add_data('https://ithelp.ithome.com.tw/users/20105707/ironman/7110')
matrix = qr.get_matrix()

QR_COLOR = wb.WHITE
BG_COLOR = wb.BLACK  

W = 160
H = 128

wb.cls(BG_COLOR)

for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        color = QR_COLOR if matrix[y][x] else BG_COLOR
        wb.pix(x * 3, y * 3, color)  # 放大每个像素

wb.box(0, H - 20, W, H, BG_COLOR)
wb.str("QR Code", 5, H - 15, 2, 2)
