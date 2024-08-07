# 05_06. 隨機產生 0 ~ 100 的整數，計算全距、平均值、眾數、標準差與四分位數。
import random
import math

# 生成 0 到 100 之間的 100 個隨機整數
data = [random.randint(0, 100) for _ in range(100)]

# 計算全距（Range）
range_value = max(data) - min(data)

# 計算平均值（Mean）
def mean(data):
    return sum(data) / len(data)

mean_value = mean(data)

# 計算眾數（Mode）
def mode(data):
    frequency = {}
    for item in data:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]
    return modes

mode_values = mode(data)

# 計算標準差（Standard Deviation）
def stdev(data, mean_value):
    variance = sum((x - mean_value) ** 2 for x in data) / (len(data) - 1)
    return math.sqrt(variance)

std_dev = stdev(data, mean_value)

# 計算四分位數（Quartiles）
def quantiles(data, n):
    sorted_data = sorted(data)
    k = len(sorted_data)
    return [sorted_data[int(i * k / n)] for i in range(1, n)]

q1, q3 = quantiles(data, 4)[0], quantiles(data, 4)[2]

# 印出所有隨機數據
print("Random Data: " + ", ".join(map(str, data)))
print(f"Data Range: {range_value}")
print(f"Mean: {mean_value:.2f}")
print(f"Mode: {', '.join(map(str, mode_values))}")
print(f"Standard Deviation: {std_dev:.2f}")
print(f"First Quartile (Q1): {q1:.2f}")
print(f"Third Quartile (Q3): {q3:.2f}")