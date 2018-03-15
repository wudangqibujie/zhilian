headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
import requests
dic = None
def proxy(func):
    def wrapper():
        global dic
        dic={"http":"http://127.0.0.1"}
        return func()
    return wrapper


@proxy
def A():
    print(dic)


A()




