import requests
import json


class ProxyChecker():
    # Check if proxy is working
    def checkProxy(self, ptype, proxyip):
        if ptype == "https":
            proxy = {"https": "https://" + proxyip}
        elif ptype == "http":
            proxy = {"https": "https://" + proxyip}
        elif ptype == "socks5":
            proxy = {"http": "socks5h://" + proxyip, "https": "socks5h://" + proxyip}
        elif ptype == "socks4":
            proxy = {"http": "socks4://" + proxyip, "https": "socks4://" + proxyip}

        Session = requests.Session()
        response = Session.get('https://google.com', proxies=proxy, timeout=5)
        if response.status_code == 200:
            return ptype
        else:
            return ""

    # Validate proxy type
    def verifyProxy(self, proxy):
        proxy_type = "Invalid"
        proxy = proxy.replace(" ", "")
        proxy = proxy.replace("\n", "")
        print("Verifying proxy: {}".format(proxy))

        try:
            proxy_type = self.checkProxy("socks5", proxy)
        except:
            try:
                proxy_type = self.checkProxy("socks4", proxy)
            except:
                try:
                    proxy_type = self.checkProxy("https", proxy)
                except:
                    try:
                        proxy_type = self.checkProxy("http", proxy)
                    except:
                        pass
        if proxy_type != "Invalid":
            print("Proxy {} is valid and it's type is {}".format(proxy, proxy_type))
        else:
            print("Proxy {} is dead or not responding.".format(proxy))

    def checkList(self):
        with open('./proxies.txt', 'r') as f:
            for line in f:
                self.verifyProxy(line)


checker = ProxyChecker()
checker.checkList()
