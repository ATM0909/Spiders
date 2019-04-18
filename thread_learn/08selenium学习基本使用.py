from selenium import webdriver
import time
from lxml import etree
from selenium.webdriver.common.by import By




driver_path = r"E:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')



# 隐式等待
# driver.implicitly_wait(10)
# inputTag = driver.find_element(By.ID,"cdcc")  # 10s找不到报错

# 显式等待
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
# try:
#     element = WebDriverWait(driver, 10).until(
#         ec.presence_of_element_located((By.ID,"cdhvc"))  # 元组
#     )
# finally:
#     driver.quit()


# cookie操作
# for i in driver.get_cookies(): # 返回列表形式
#     print(i)
# print("--"*30)
# print(driver.get_cookie("BAIDUID")) # 指定value值
# driver.delete_all_cookies()
# driver.delete_cookie("BAIDUID")



#  行为链
"""
from selenium.webdriver.common.action_chains import ActionChains
.context_click() # 右键点击
.click_and_hold() # 点击不松开
.double_click() # 双击

"""
# actions = ActionChains(driver)
# actions.move_to_element(inputTag)
# actions.send_keys_to_element(inputTag, "python")
# actions.move_to_element(submitTag)
# actions.click(submitTag)
# actions.perform()
