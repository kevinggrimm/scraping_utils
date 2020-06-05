#!/usr/bin/python3

import re
import random
import requests
import time

from bs4 import BeautifulSoup as bs
from itertools import cycle
#from requests.adapters import HTTPAdapter
#from requests.packages.urllib3.util.retry import Retry
#from requests_toolbelt import sessions
#from requests_toolbelt.utils import dump

import settings

class Proxy():
    
    def __init__(self):
        url = "https://free-proxy-list.net/"
        r = requests.get(url)
        soup = bs(r.content, "html.parser")
        rows = soup.find("tbody").find_all("tr")
        self.rows = rows
        
    def get_proxies(self):
        proxies = set()
        for row in self.rows:
            ip = row.find_all("td")[0].get_text()
            port = row.find_all("td")[1].get_text()
            proxy = ":".join([ip, port])
            proxies.add(proxy)
        self.proxies = proxies
    
    def create_proxy_pool(self):
        proxy_pool = cycle(self.proxies)
        self.proxy_pool = proxy_pool
        
    def get_next_proxy(self):
        proxy = next(self.proxy_pool)
        return proxy 


# proxy_class = Proxy()
# proxy_class.get_proxies()
# proxy_class.create_proxy_pool()

# for i in range(1, 20): 
#     try: 
#         proxy = proxy_class.get_next_proxy()
#         proxies = {'http': proxy, 'https': proxy}
#         r = requests.get(full_url, headers=headers, proxies=proxies, timeout=10)
#         print(r.status_code)
#         if r.status_code == 200:
#             break
#     except Exception as e:
#         print(e)
#         pass