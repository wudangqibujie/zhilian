import requests
import random
from selenium import webdriver
import time

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
proxies=None
# ip_pool=None
# ip="127.0.0.1"
def get_ip(filename):
    f = open(filename)
    ip_pool = f.readlines()
    def get_ip_pool():
        nonlocal ip_pool
        ip_pool = [i.strip() for i in ip_pool]
        return ip_pool
    return get_ip_pool

ip_pool = get_ip("ip_list_http.txt")

def ip_daili(func):
    def wrapper(url):
        ip = random.choice(ip_pool())
        global proxies
        proxies = {"http":"http://"+ip}
        return func(url)
    return wrapper

#加代理IP
# @ip_daili
def common_get(url):
    try:
        r = requests.get(url,headers=headers,proxies = proxies)
        if r.status_code == 200:
            return r.text
        else:
            print("相应码异常")
    except:
        print("请求异常！")

#用模拟浏览器获取html
SECOND=1
def moni_browser(url,prov):
    global SECOND
    browser = webdriver.Chrome()
    browser.get(url)
    seconds = 1
    if SECOND <10:
        try:
            time.sleep(SECOND)
            assert prov in browser.title
            html = browser.page_source
            print("获取HTML成功")
            return html
        except:
            SECOND +=1
            print("HTML未渲染出！")
            return moni_browser(url,prov)
    else:
        print("目标HTML获取有误！")

# moni_browser("http://www.python.org","Python")




if __name__ == '__main__':
    common_get("http://www.baidu.com")




