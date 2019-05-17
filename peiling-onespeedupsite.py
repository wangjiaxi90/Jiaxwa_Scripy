import request
import win32api
import win32con
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
import time
import re


from bs4 import BeautifulSoup
from lxml import etree
chromedriver = r'C:\Users\v-jiaxwa\AppData\Local\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(executable_path=chromedriver)
pa = "C:\\Users\\v-jiaxwa\\Desktop\\4\\"
ls = ['pop', 'rock', 'rap', 'jazz', 'blues', 'classic', 'rnb soul', 'bluegrass', 'country', 'gospel', 'opera', 'folk', 'punk', 'disco']
for url in ls:
    if(os.path.exists(pa+url) == False):
        os.makedirs(pa+url)
    #进入pop
    browser.get(r'https://freemidi.org/genre-'+url)
    #得到所有艺术家的名字
    r1 = browser.find_elements_by_xpath("//*[@id='mainContent']/div[@class='genre-band-container']/div/a[2]")
    #下面for循环是遍历艺术家的名字
    for i in range(len(r1)):
        #建立对应艺术家名字的folder
        h1 = r1[i].get_attribute('href')
        h1n = r1[i].text
        h1n = str(h1n).replace(' ', '')
        if (os.path.exists(pa + url + "\\" + h1n) == False):
            os.makedirs(pa + url + "\\" + str(h1n))
        #进入这个网站  1927k
        browser.get(h1)

        r2 = browser.find_elements_by_xpath("//*[@id='mainContent']/div[1]/div[2]/div[1]/div/div/span/a")
        for j in range(len(r2)):
            h2 = r2[j].get_attribute('href')  # 非常重要
            h2n = r2[j].text
            h2n = str(h2n).replace(' ', '')
            path=pa + url + "\\" + h1n + "\\" + h2n
            if (os.path.exists(path) == False):
                os.makedirs(path)
            browser.get(h2)
            print(path)


            #下面是点击操作


            ActionChains(browser).context_click(browser.find_element_by_xpath('// *[ @ id = "downloadmidi"]')).perform()
            time.sleep(1.5)
            win32api.keybd_event(75, win32con.KEYEVENTF_KEYUP, 0)
            os.system(r'C:\Users\v-jiaxwa\Desktop\Autolt.exe ' + path + "\\" + h2n + ".mid")
            time.sleep(10)
            ActionChains(browser).context_click(browser.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div/div[1]/div[3]/a[2]')).perform()
            time.sleep(1.5)
            win32api.keybd_event(75, win32con.KEYEVENTF_KEYUP, 0)
            os.system(r'C:\Users\v-jiaxwa\Desktop\Autolt.exe ' + path + "\\" + h2n + ".mp3")
            time.sleep(10)
        print(h1n)

print('Done!')
