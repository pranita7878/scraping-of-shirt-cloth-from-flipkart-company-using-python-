from selenium import webdriver
from  bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import requests
from openpyxl import Workbook
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

url = 'https://www.flipkart.com/' 
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)
driver.get(url)
# Find the search input and enter the product name

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("full sleeve XL tshirt for women under 300")
search_box.send_keys(Keys.RETURN)

# Wait for search results to load

time.sleep(2)
soup = BeautifulSoup(driver.page_source,'html5lib')
# print(soup.prettify())
driver.close()

image = soup.find_all('img',class_='_53J4C-')
images=[]
for i in range(0,len(image)):
        images.append(image[i])
print(images) 
print(len(images))
print('********************************************')

title=soup.find_all('a',class_='WKTcLC')
titles=[]
for i in range(0,len(title)):
        titles.append(title[i].get_text())
print(titles) 
print(len(titles))
print('********************************************')
