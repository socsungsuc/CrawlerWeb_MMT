import numpy as np
from selenium import webdriver
from time import sleep
import random
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import pandas as pd

# Declare browser
from selenium.webdriver.chrome.service import Service
service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)

title = []
links = []
price = []

for pid in range(4,10):
    # open url
    driver.get("https://www.lazada.vn/dien-thoai-di-dong/?page={}&spm=a2o4n.home.cate_1.1.723b3bdcar9DXX".format(pid))
    sleep(random.randint(5,10))

    # ================================ GET Product Names and links
    elems = driver.find_elements(By.CSS_SELECTOR , ".RfADt [href]")
    title += [elem.text for elem in elems]
    links += [elem.get_attribute('href') for elem in elems]

    # ================================ GET Product Prices
    elems_price = driver.find_elements(By.CSS_SELECTOR , ".aBrP0")
    len(elems_price)
    price += [elem_price.text for elem_price in elems_price]

df = pd.DataFrame(list(zip(title, price, links)), columns = ['title', 'price','link_item'])
df['index_']= np.arange(1, len(df) + 1)
df.to_csv('product_info.csv', index=False)