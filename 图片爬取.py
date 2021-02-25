#自动图片爬取器
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import math
import time

url = "https://image.baidu.com/" #图片搜索引擎
pictureType = r"hello,world" #图片关键字
num = 100  #图片数量 实际数量会有点出入
Folder = r"C:\Users\stone\Desktop\代码\python\图片"
'''
把关键字放入输入框，搜索
'''
driver = webdriver.Edge()
driver.get(url)
inputUi = driver.find_element_by_id("kw")
inputUi.send_keys(pictureType)
time.sleep(1)
inputUi.send_keys(Keys.ENTER) #按回车代替点击

'''
根据需要的图片个数计算下滑次数并下滑页面
'''
num = num - 15 #一进到网站就会有15张图片，这些不需要下滑
num= math.ceil(num/15) #下滑一次约可以加载15张图片，计算需要的下滑次数
#math.ceil() 进一法取整

for i in range(num):
    driver.find_element_by_tag_name("body").send_keys(Keys.SPACE) #按一下空格来下滑

'''
获取图片的url
'''
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

'''
用requests获取图片二进制文本，并写入文件
'''

for (url,index) in zip(urlList,range(1,len(urlList))):
	path = Folder+r"\%s%d.jpg"%(pictureType,index)
	
	for i in range(5):
	    try:
	        r = requests.get(url)
	        break
	    except:
	    	pass
	    	
	else:
		print("-"*40+"\n"+"第%d张:" %(index)+url+"\n状态:<请求失败>")
		continue
		
	print("-"*40+"\n"+"第%d张:" %(index)+url+"\n状态:<请求成功>")
	
	with open(path,"wb") as f:
		f.write(r.content)
		
else:	
    print("bye!")

