import json

# 打开一个JSON文件
with open("masterpiece/image_information.json", 'r+', encoding='utf-8') as f:
    data = json.loads(f.read())

# 输出转换后的Python对象
print(data)