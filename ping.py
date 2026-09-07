import time
import random
import requests

# 1. 设置随机休眠时间（例如：随机等待 1 到 300 秒之间）
# 配合 GitHub Actions 的定时，能让最终访问链接的时间完全随机化
sleep_time = random.randint(1, 300)
print(f"随机休眠 {sleep_time} 秒后将访问链接...")
time.sleep(sleep_time)

# 2. 配置你需要访问的链接
url = "https://your-target-url.com"  # 👈 替换为你的目标链接

try:
    # 模拟浏览器发送请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers, timeout=10)
    print(f"访问成功！状态码: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"访问失败，错误信息: {e}")
