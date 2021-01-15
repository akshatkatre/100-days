from selenium import webdriver
import time
from bs4 import BeautifulSoup
driver = webdriver.Chrome("/Users/akshat/repo/chromedriver/chromedriver")
driver.get(url="https://www.listennotes.com/podcasts/heisenbook-20-heisenbook-ny0L7ixPAob/")


# button = driver.find_element_by_css_selector('.btn')
def click_load_more():
    button = driver.find_element_by_xpath('//*[@id="episodes-pagination"]/div/div/button')

    for i in range(30):
        button.click()
        print(f'clicked {i}')
        time.sleep(2)

soup = BeautifulSoup()

