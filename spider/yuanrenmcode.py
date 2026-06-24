import requests
import time
import hashlib


def get_m():
    t = int(time.time() * 1000) + 1000


    md5_str = hashlib.md5(str(t).encode('utf-8')).hexdigest()

    return f"{md5_str}|{t}"
print(get_m())

"""
headers = {
    "User-Agent": "yuanrenxue.project",
    "Referer": "https://match.yuanrenxue.com/match/1"
    }

for page in range(1,6):
    params = {
        "page": page,
        "m": get_m()
    }
    res = requests.get("https://match.yuanrenxue.com/api/match/1", headers=headers, params=params)
    print(res.json())
"""
