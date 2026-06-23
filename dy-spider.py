import requests     # 响应爬取
from DrissionPage import ChromiumPage   # 谷歌
import re   # 正则表达式
import os   # 系统操作

# 创建文件夹
os.makedirs((r"D:\爬虫视频"), exist_ok=True)
    
# 伪装信息
headers={"cookie": os.environ.get("DOUYIN_COOKIE"),
         "referer":"https://www.douyin.com/user/MS4wLjABAAAAsnVIdQ1WQGS4OjERohiH5GJfJl9-OV4SHc2urt-RHnik0LQJbYpz_ZMMR-k8eiHf?from_tab_name=main&vid=7650113124381861349",
         "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
         }


GG = ChromiumPage()     # 自动打开网页
GG.listen.start("aweme/post/")  # 监听数据
GG.get("https://www.douyin.com/user/MS4wLjABAAAAsnVIdQ1WQGS4OjERohiH5GJfJl9-OV4SHc2urt-RHnik0LQJbYpz_ZMMR-k8eiHf?enter_from=author_card&from_gid=7650113124381861349&from_tab_name=main&tab_name=like&vid=7650113124381861349")
sjb = GG.listen.wait()  # 等待监听


jason = sjb.response.body   # 处理数据
date = jason["aweme_list"]  # 找数据包中的视频


for i in date:
    video_url = i["video"]["play_addr"]["url_list"][0]  # 获取详细内容
    title = i["desc"]   #标题
    title_re = re.sub("[,.<>?;=-]", "", title)     # 视频命名格式
    print(f"正在下载内容{title_re}")
    
    res = requests.get(url = video_url,headers = headers).content # 发送请求

    with open(r"D:\爬虫视频\\" + title_re + ".mp4", "wb") as f:
        f.write(res)
