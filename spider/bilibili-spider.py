import requests #导入请求模块
from moviepy.editor import * #导入处理视频音频模块

#伪装信息
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
         "referer":"https://www.bilibili.com/video/BV1X37c6vEcB/?spm_id_from=333.1007.tianma.1-1-1.click",
         }

#视频url网址
url="https://cn-gddg-ct-01-11.bilivideo.com/upgcxcode/86/93/39298859386/39298859386_qe1-1-100023.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&platform=pc&trid=0000d0665c573195440f86587b588db735bu&gen=playurlv3&og=cos&deadline=1782403504&oi=1946803821&uipk=5&mid=0&nbs=1&os=bcache&upsig=946e929a29ad6af909351f36a6d9333e&uparams=e,platform,trid,gen,og,deadline,oi,uipk,mid,nbs,os&cdnid=61311&bvc=vod&nettype=0&bw=537724&lrs=94&f=u_0_0&qn_dyeid=4900027dc0cb410c00e3eac16a3d3590&agrr=0&buvid=E5D120FF-707F-3288-B79A-DF58CB03F44172015infoc&build=0&dl=0&orderid=0,3"

#发送请求
res = requests.get(url,headers = headers)

#保存视频
open("视频.mp4","wb").write(res.content)

#音频获取
url="https://cn-gddg-ct-01-10.bilivideo.com/upgcxcode/86/93/39298859386/39298859386_qe1-1-30216.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&os=bcache&og=cos&platform=pc&uipk=5&mid=0&oi=1946803821&gen=playurlv3&trid=0000b6b7e01ed60b4e69b7ddf71afc14235u&deadline=1782402718&nbs=1&upsig=aa122e7aaf7f6667d10be6f1c6ba8592&uparams=e,os,og,platform,uipk,mid,oi,gen,trid,deadline,nbs&cdnid=61310&bvc=vod&nettype=0&bw=66413&lrs=94&qn_dyeid=3f954d943d32d5a500b51be56a3d327e&agrr=0&buvid=E5D120FF-707F-3288-B79A-DF58CB03F44172015infoc&build=0&dl=0&f=u_0_0&orderid=0,3"

#发送请求
res = requests.get(url,headers = headers)

#保存音频
open("音频.mp3","wb").write(res.content)


#处理视频音频
video = VideoFileClip("视频.mp4")
audio = AudioFileClip("音频.mp3")

#合并音频
sp = video.set_audio(audio)

#保存视频
sp.write_videofile("破站视频.mp4")

