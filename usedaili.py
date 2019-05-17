import random, requests
from lxml import etree
import json
import os,sys


class GetHtml:
    def __init__(self):
        self.user_agent = [
            "Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.11.2 UWS/2.11.0.33 Mobile Safari/537.36",
            "Mozilla/5.0 (iPad; CPU OS 10_3_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) BaiduHD/5.4.0.0 Mobile/10A406 Safari/8536.25",
            "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36",
            "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; BLN-AL10 Build/HONORBLN-AL10) AppleWebKit/537.36 (KHTML, like Gecko) MQQBrowser/7.3 Chrome/37.0.0.0 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; BND-AL10 Build/HONORBND-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.0.0.980 Mobile Safari/537.36"
        ]
        self.path = '..\\verified_proxies.json'
        self.PROXIES_LIST = self.get_proxies_list()

    def get_user_agent(self):
        return random.choice(self.user_agent)

    def get_proxies_list(self):
        PROXIES_LIST = []
        with open(self.path, 'r') as f:
            proxiesjson = f.readlines()
            for proxiejson in proxiesjson:
                proxiesdict = json.loads(proxiejson)
                PROXIES_LIST.append(proxiesdict)
        return PROXIES_LIST

    def get_header_proxie(self):
        user_agent = self.get_user_agent()
        header = {"User-Agent": user_agent}
        proxie = random.choice(self.PROXIES_LIST)
        return header, proxie

    def get_html(self, url,**kwargs):
        while 1:
            header, proxie = self.get_header_proxie()
            # , proxies = proxie
            try:
                response = requests.get(url, headers=header,params=None,**kwargs)
            except:
                pass
            else:
                break
        data = response.text
        return data

    def get_proxies(self,url):
        for i in range(len(self.PROXIES_LIST)):
            print(i)
            proxie = self.PROXIES_LIST[i]
            if i == 0:
                os.remove(self.path)
            try:
                response = requests.get(url, headers={"User-Agent": self.get_user_agent()},proxies = proxie, params=None,timeout=3)
            except:
                continue
            if response.status_code == 200:
                with open(self.path, 'a+') as f:
                    json_str = json.dumps(proxie)
                    f.write(json_str + '\n')



if __name__ == '__main__':
    get_pro = GetHtml()
    url = 'http://en.midimelody.ru'
    get_pro.get_proxies(url)