import os
import time
import win32api
import requests
import win32con
from bs4 import BeautifulSoup
import json
from lxml import etree
from selenium import webdriver
import copy
import re

from selenium.webdriver import ActionChains

chromedriver = r'C:\Users\v-jiaxwa\AppData\Local\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(executable_path=chromedriver)

browser.get('http://en.midimelody.ru/category/midi-melodies/')
last_url = browser.current_url
basepath = r'C:\Users\v-jiaxwa\Desktop\4'
mapname = {}
pagenum = 1
while 1:
    try:
        try:
            print('pagenum：' + str(pagenum))
        except:
            print('pagenum')
        # 下一页XPath //*[@id="content"]//a[@class="next page-numbers"]
        lsdown_page = browser.find_elements_by_xpath('//h3/a')
        thisurl = browser.current_url
        for k in range(len(lsdown_page)):
            try:
                print('item:' + str(k+1))
            except:
                print("item")
            lsdown_page[k].click()
            templs = browser.find_elements_by_xpath('//div[@class="div_tab_rows"]/p')
            str_name = ''
            for i in range(len(templs)):
                if i % 3 == 0:
                    str_name = templs[i].text
                    str_name = re.sub(r"[^A-Za-z0-9.\-]", '', str_name).replace(".mid", '')
                    if str_name in mapname.keys():
                        str_name = mapname[str_name] + 1
                    else:
                        mapname[str_name] = 0
                elif i % 3 == 2:
                    try:
                        print('第 ' + str(i / 3 + 1) + ' 个')
                    except:
                        print("MouGe")
                    ActionChains(browser).context_click(templs[i]).perform()
                    time.sleep(1.2)
                    win32api.keybd_event(75, win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(0.5)
                    os.system(r'C:\Users\v-jiaxwa\Desktop\Autolt.exe ' + basepath + "\\" + str_name + '.mid')
                    time.sleep(1.2)
            browser.get(thisurl)
            lsdown_page = browser.find_elements_by_xpath('//h3/a')
            time.sleep(1.2)
        time.sleep(1.2)
        next = browser.find_element_by_xpath('//*[@id="content"]//div[@class="navigation"]/a[@class="next page-numbers"]')
        next.click()
        pagenum = pagenum + 1
    except Exception as arr:
        print(arr.args)

print("Done!")