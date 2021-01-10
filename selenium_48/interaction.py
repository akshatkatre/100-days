from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

URL = "https://en.wikipedia.org/wiki/Main_Page"
CHROME_DRIVER_PATH = "/Users/akshat/repo/chromedriver/chromedriver"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(url=URL)

# english_article_count = driver.find_element_by_css_selector("#articlecount a")
# print(english_article_count.text)
# english_article_count.click()

# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

search_bar = driver.find_element_by_name("search")
search_bar.send_keys("Python")
time.sleep(1)
search_bar.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()
