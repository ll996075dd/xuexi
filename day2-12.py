import requests
import os
import time
import urllib3  #这个纯粹防止warning提示，没啥作用
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#获取返回网页源码
def gethtml(url):
    headers={
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 6.0.1; BLA-AL00 Build/V417IR)",
    "Host": "imgapp.iimzt.com",
    "Referer": "https://app.mmzztt.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    }
    r=requests.get(url,headers=headers,verify=False)
    
    return r

#下载图片
def downimg():
    for num1 in range(1,100):
        if num1<10:
            num1="0"+str(num1)
        else:
            num1=str(num1)
        for abnum in range(2):
            if abnum == 0:
                ab="a"
            elif abnum ==1:
                ab="b"
            for num2 in range(1,999):
                if num2<10:
                    num2="0"+str(num2)
                else:
                    num2=str(num2)

                #先判断路径再访问，节省重复宽带,跳过已存在文件
                savepath=rootpath+"\\"+str(year)+"\\"+str(month)+"\\"+str(num1)+str(ab)+"\\"
                imgpath=savepath+str(num2)+".jpg"
                
                #如果文件存在则跳过
                if os.path.exists(imgpath):
                    continue
                #访问图片
                url="https://imgapp.iimzt.com/"+str(year)+"/"+str(month)+"/"+str(num1)+str(ab)+str(num2)+".jpg"
                r=gethtml(url)
                if r.status_code !=200:
                    print(f"获取url：{url}失败!,跳出循环进入下一层")
                    #尾数尽头则跳出循环，进行下一层
                    break
                elif r.status_code ==200:
                    #如果没有目录则创建
                    if not os.path.exists(savepath):
                        os.makedirs(savepath)
                    with open(imgpath, "wb") as f:
                        f.write(r.content)
                    print(f"{str(year)}年{str(month)}月,已写入{str(num1)}{str(ab)}{str(num2)}.jpg")
                    #延时多少秒访问下一张
                    time.sleep(tsleep)
    print("======已全部爬取结束，请查收======")

if __name__ == "__main__":
    #这里自己设置年月和下载根目录
    global year,month,rootpath,tsleep
    year="2020"                 #年
    month="08"                  #月
    rootpath="D:\\妹子图"       #下载根目录
    tsleep=0.8                  #下载延时，建议在0.5~2秒一张，太快可能被封ip
    #开始下载
    downimg()