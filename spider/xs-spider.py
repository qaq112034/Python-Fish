import requests
from bs4 import BeautifulSoup



headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0"}

url = "https://b.faloo.com/1525090.html?1"

response = requests.get(url,headers = headers)

soup = BeautifulSoup(response.text,"html.parser")

chapter_list = soup.select(".DivTd3")

for i in range(20):
    chapter_name = chapter_list[i].select_one("a").text
    chapter_url = "https:" + chapter_list[i].select_one("a").get("href")
    details_response = requests.get(chapter_url,headers = headers)
    details_soup = BeautifulSoup(details_response.text,"html.parser")
    p_list = details_soup.select(".noveContent>p")
    

    try:
        for p in p_list:
            with open(chapter_name + ".txt", "a+", encoding = "utf-8") as f:
                f.write(p.text + "\n")
        print(chapter_name + "成功下载")
    except FileNotFoundError as e:
        continue
