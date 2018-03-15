import requests
url1 = "https://www.kuaidaili.com/free/inha/2/"
url2 = "https://www.kuaidaili.com/free/inha/3/"
import time
r = requests.get(url1)
print(r.status_code)
time.sleep(1)
r = requests.get(url2)
print(r.status_code)
