from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s=Service('/home/sanhita/Downloads/chromedriver')
driver=webdriver.Chrome(service=s)
driver.get("https://forms.gle/TMYuntJLnq7T5RH87")
time.sleep(2)


# def first_name(firstName):
firstName="sanhita"
first=driver.find_element_by_class_name("whsOnd.zHQkBf")
first.send_keys(firstName)

lastName="kundu"
last=driver.find_element_by_class_name("whsOnd.zHQkBf")
last.send_keys(lastName)