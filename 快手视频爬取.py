#快手视频爬取
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time
import os
import sys

url = input("请输入视频网址:")

try:
    driver = webdriver.Edge()
    driver.get(url)
    time.sleep(2)
    video = driver.find_element_by_class_name("player-video")
    src = video.get_attribute("src")
    time.sleep(2)
    driver.quit()
except:
    print("出现问题!")
    driver.quit()
    sys.exit(1)
    
    
os.system("cls")
print("已经找到视频，网址："+src+"\n")
for i in range(10):
    try:
        r = requests.get(src)
        print("成功请求视频网址!")
        break
    except:
        print("重连第%d次……" %(i))
else:
    print("出现问题!")
    sys.exit(1)
    
path = r"C:\Users\stone\Desktop\代码\python\视频\%s.mp4" %(input("请输入保存视频名（不用带后缀）："))
with open(path,"wb") as f:
    f.write(r.content)
