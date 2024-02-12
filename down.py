import os
import requests
from tqdm import tqdm

platform = "android"
#platform = "ios"

# 基础 URL
base_url = f"https://cdn.megagamelog.com/cross/release/{platform}/curr_1/Custom/"

# 读取文件
with open("ilist.txt", "r", encoding='utf-8-sig') as file:
    items = file.read().split(',')

# 下载文件
for item in tqdm(items):
    url = base_url + item
    response = requests.get(url)
    
    # 将文件保存到本地
    dir = "custom"
    os.makedirs(dir, exist_ok=True)
    with open(f"{dir}/{item}", 'wb') as f:
        f.write(response.content)
