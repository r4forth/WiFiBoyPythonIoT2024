import json

# 範例 JSON 字串
json_string = '{"name": "Daniel", "age": 44, "isStudent": false, "courses": ["math", "science"]}'

# 解析 JSON 字串為 Python 字典
data = json.loads(json_string)

# 輸出解析後的資料
print("解析後的資料:", data)
print("名字:", data["name"])
print("年齡:", data["age"])
print("是否為學生:", data["isStudent"])
print("課程列表:", data["courses"])

# 修改資料
data["age"] = 45
data["isStudent"] = True
data["courses"].append("history")

# 將 Python 字典編碼為 JSON 字串
new_json_string = json.dumps(data)

# 輸出新的 JSON 字串
print("新的 JSON 字串:", new_json_string)