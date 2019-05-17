import telnetlib
import json
import requests


class GetProxy:
    c = 5
    print(c)

    def __init__(self, savePath):
        self.proxy_url = 'https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list'
        self.path = savePath

    def getProxy(self):
        response = requests.get(self.proxy_url)
        proxies_list = response.text.split('\n')
        for proxy_str in proxies_list:
            proxy_json = json.loads(proxy_str)
            host = proxy_json['host']
            port = proxy_json['port']
            type = proxy_json['type']
            self.verify(host, port, type)

    def verify(self, ip, port, type):
        try:
            telnet = telnetlib.Telnet(ip, port=port, timeout=3)
        except:
            print('unconnected')
        else:
            dict = {type: str(ip) + ':' + str(port)}
            proxiesJson = json.dumps(dict)
            with open(self.path, 'a+') as f:
                f.write(proxiesJson + '\n')
            print("已写入：%s" % dict)


if __name__ == '__main__':
    savepath = '../verified_proxies.json'
    proxy = GetProxy(savepath)
    proxy.getProxy()
