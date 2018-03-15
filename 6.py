from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.python.org")
# time.sleep(4)
print(driver.title)
try:
    assert "sfwergergerge" in driver.title
    print("OK")
except:
    print("chucuol ")
