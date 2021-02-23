from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import math
import time

url = "https://image.baidu.com/" #图片搜索引擎
pictureType = r"hello,world" #图片关键字
num = 100  #图片数量 实际数量会有点出入

driver = webdriver.Edge()
driver.get(url)
inputUi = driver.find_element_by_id("kw")
inputUi.send_keys(pictureType)
time.sleep(1)
inputUi.send_keys(Keys.ENTER)

for i in range(0,math.ceil(num/36)):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(1)

imgLogList = driver.find_elements_by_class_name("main_img")

urlList = []
for Log in  imgLogList:
	url = Log.get_attribute("src")
	if "emoji.cdn.bcebos.com" in url:
		pass
	elif len(url) > 180:
		pass
	else:
		urlList.append(url)
else:
	driver.quit()
	
No = []
Yes = []
for (url,index) in zip(urlList,range(1,len(urlList))):
	path = r"C:\Users\stone\Desktop\代码\python\图片\%s%d.jpg"%(pictureType,index)
	
	for i in range(5):
	    try:
	        r = requests.get(url)
	        break
	    except:
	    	pass
	else:
		print("-"*40+"\n"+"第%d张:" %(index)+url+"\n状态:<请求失败>")
		No.append("+")
		continue
		
	print("-"*40+"\n"+"第%d张:" %(index)+url+"\n状态:<请求成功>")
	Yes.append("+")
	with open(path,"wb") as f:
		f.write(r.content)
		
else:	
    print("这次共找到%d张图片:%d张获取失败 %d张获取成功" %(len(urlList),len(No),len(Yes)))
    print("bye!")
