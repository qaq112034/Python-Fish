import requests

def get_weather():
    city = input("请输入城市名称：")
    
    # 国内稳定免费接口，不需要任何API Key
    url = f"https://api.66api.cn/api/weather?city={city}"

    try:
        res = requests.get(url, timeout=8)
        data = res.json()

        if data["code"] == 200:
            info = data["data"]
            print("\n===== 当前天气 =====")
            print(f"城市：{info['city']}")
            print(f"温度：{info['temp']}℃")
            print(f"天气：{info['weather']}")
            print(f"风向：{info['wind']}")
            print(f"湿度：{info['humidity']}")
        else:
            print("❌ 未找到该城市")

    except:
        print("❌ 网络异常，请重试")

get_weather()
