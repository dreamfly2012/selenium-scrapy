import time

from selenium import webdriver
from selenium.common.exceptions import *

#参数为chromedriver的路径，可以去
#https://npm.taobao.org/mirrors/chromedriver/
#下载对应版本的驱动，查看chrome版本的方式为浏览器输入
#chrome://version
driver = webdriver.Chrome("chromedriver.exe")

#定义下载张数
num = 10

#定义下载图片的名字
name = "长泽雅美"

print("浏览器启动")

driver.set_page_load_timeout(30)

try:
    driver.get("https://image.baidu.com/")
except TimeoutException:
    driver.execute_script("window.close()")

driver.find_element_by_id("kw").send_keys(name)

driver.find_element_by_class_name("s_search").click();

driver.implicitly_wait(5)

first_img = driver.find_element_by_css_selector(".main_img.img-hover")
first_img.click()
driver.implicitly_wait(5)

print(driver.window_handles)
driver.switch_to_window(driver.window_handles[1])

print("开始下载图片:")


#循环点击下一个，下载图片
#元素定位参考
#http://www.selenium.org.cn/1834.html
for i in range(num):
    driver.find_element_by_class_name("btn-download").click();
    switch_button = driver.find_element_by_css_selector(".img-next")
    print(switch_button)
    switch_button.click();
    driver.implicitly_wait(5)

#下载结束，执行过程如果没有出现错误，应该就可以正常下载文件
print("下载结束")