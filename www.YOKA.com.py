#coding=gbk
import requests
from bs4 import BeautifulSoup
import json
from lxml import etree
from selenium import webdriver
import copy


chromedriver = r'C:\Users\v-jiaxwa\AppData\Local\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(executable_path=chromedriver)


headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3469.400"}
url = "http://www.yoka.com/beauty/bodycare/2019/0513/pic52926601315916.shtml"
outpath = 'meizhuang.txt'
f = open(outpath, 'a+', encoding='utf-8')
try:
    thistitle = ''
    lasttitle = '何洁精修图原图对比明显 修图老师厉害了'
    tempstr = ''
    while(url):
        page = browser.get(url)
        html = browser.page_source
        data = etree.HTML(html)
        try:
            links = data.xpath('//*[@id="nextPic"]//@href')
            url = 'http://www.yoka.com' + links[0]
        except:
            link = ''
        tempstr += data.xpath('/html/body/div[11]/div/dl/dd/text()')
        thistitle = data.xpath('//*[@id="picTitle"]/text()')
        if(thistitle != lasttitle):
            f.writelines('title:'+lasttitle+'。'+tempstr+'@@')
            f.flush()
            lasttitle = copy.deepcopy(thistitle)
except:
    pass
f.close()
print('Done!')

