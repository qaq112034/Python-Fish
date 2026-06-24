import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=4&lang=zh"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        response.encoding = "utf-8"
        weather_info = response.text.strip()
        print(f"✅ 【{city}】天气信息：")
        print(weather_info)
    except requests.exceptions.HTTPError:
        print("❌ 错误：该城市不存在或接口访问失败")
    except requests.exceptions.ConnectionError:
        print("❌ 错误：网络连接异常")
    except Exception as e:
        print(f"❌ 异常：{e}")
        
if __name__ == "__main__":
    city_name = input("请输入查询城市：")
    get_weather(city_name)
