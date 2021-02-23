#在安全平台上胡说九道（或八道、十道）
#因安全网站有问题，没有测试代码

from selenium import webdriver
import time
import random
nonList = ["九道","八道","十道"]

driver = webdriver.Edge()
driver.get("https://www.xueanquan.com/Activity/Index.aspx?currentPage=1")
time.sleep(3)
driver.find_element_by_id("loginLinkBtn").click()

driver.find_element_by_id("loginname").send_keys("zhangshaoyi7030")
time.sleep(2)
driver.find_element_by_id("password").send_keys("Zsy083500")
time.sleep(2)

driver.find_element_by_xpath("/html/body/div[6]/div/dl[5]/a").click()

for i in range(12):
    try: 
        Xpath = "/html/body/div[3]/ul/li[%d]/a" %(i+1)
        driver.find_element_by_xpath(Xpath).click()    #通过有规律的Xpath进入课程
        try: 
            driver.find_element_by_partial_link_text("我要留言").click()
            time.sleep(1)
            nonsense = nonList[random.randint(0,len(nonList)-1)]
            driver.find_element_by_id("DB").send_keys(nonsense)
            print(driver.current_url+"："+nonsense)
            time.sleep(1)
            driver.find_element_by_id("rad").click()
            time.sleep(1)
            driver.find_element_by_id("btnSubmit").click()
        except:#若没有留言系统
            pass
    except:
        pass
else:
	driver.quit()
