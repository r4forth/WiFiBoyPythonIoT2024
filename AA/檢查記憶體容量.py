# 檢查記憶體容量
import micropython
print(micropython.mem_info())

# 檢查 Flash 容量
import esp
print(esp.flash_size()/1024/1024)