#%%
from selenium import webdriver
from time import sleep

#%%
# 后面是浏览器驱动位置，记得前面加r'','r'是防止字符转义的
driver = webdriver.Chrome()

#%%
# 用get打开百度页面
driver.get("http://www.baidu.com")

#%%
# 找到百度的输入框，并输入 美女
driver.find_element_by_id('kw').send_keys("美女")
# sleep(2)

#%%
# 点击搜索按钮
driver.find_element_by_id('su').click()
# sleep(2)

#%%
# 在打开的页面中找到“Selenium - 开源中国社区”，并打开这个页面
driver.find_elements_by_link_text('美女_海量精选高清图片_百度图片')[0].click()
# sleep(3)

#%%
# 关闭浏览器
driver.quit()

# %%
