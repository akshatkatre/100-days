from selenium import webdriver

URL = "https://en.wikipedia.org/wiki/Main_Page"
CHROME_DRIVER_PATH = "/Users/akshat/repo/chromedriver/chromedriver"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(url=URL)

english_article_count = driver.find_element_by_css_selector("#articlecount a")
print(english_article_count.text)

driver.quit()
