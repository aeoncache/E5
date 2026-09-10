import time
import random
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 1. 随机休眠 0 到 7200 秒（即 0 到 2 小时）
# 配合 GitHub Actions 每小时的触发，可以完美实现 1 ~ 3 小时的随机区间
sleep_time = random.randint(0, 7200)


# 随机休眠
sleep_time = random.randint(0, 7200)
hours = sleep_time // 3600
minutes = (sleep_time % 3600) // 60
print(f"触发成功！本次将随机休眠 {hours} 小时 {minutes} 分钟 ({sleep_time} 秒) 后访问链接...")
time.sleep(sleep_time)

url = "https://172.245.168.140/"
try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers, timeout=10, verify=False)
    print(f"✅访问成功！状态码: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"❌访问失败，错误信息: {e}")

