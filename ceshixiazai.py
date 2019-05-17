import re

import requests
from lxml import etree

mapname = {}
basepath = r'C:\Users\v-jiaxwa\Desktop\4'
r1 = requests.get('http://en.midimelody.ru/category/midi-melodies/')
while 1:
    html = r1.text
    data = etree.HTML(html)
    ls_downpage = data.xpath('//h3/a/@href')

    for k in range(len(ls_downpage)):
        r2 = requests.get(ls_downpage[k])
        data2 = etree.HTML(r2.text)
        templs = data2.xpath('//div[@class="div_tab_rows"]/p/span/a')
        str_name = ''
        for i in range(len(templs)):
            str_name = templs[i].text
            str_name = re.sub(r"[^A-Za-z0-9.\-]", '', str(str_name)).replace(".mid", '')
            if str_name in mapname.keys():
                str_name = mapname[str_name] + 1
            else:
                mapname[str_name] = 0
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31'}
            headers.update({"Referer": ls_downpage[k]})
            r = requests.get('http://en.midimelody.ru'+str(templs[i].xpath('@href')[0]),
                             timeout=5,
                             headers=headers)
            with open(basepath + '\\' + str(str_name) + '.mid', 'wb') as f:
                print(str(str_name))
                f.write(r.content)
    try:
        next_url = data.xpath('//*[@id="content"]//div[@class="navigation"]/a[@class="next page-numbers"]/@href')[0]
        r1 = requests.get(next_url)
    except:
        break
print("Done!")
