from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

URL = "http://secure-retreat-92358.herokuapp.com/"
CHROME_DRIVER_PATH = "/Users/akshat/repo/chromedriver/chromedriver"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(url=URL)

# fname = driver.find_element_by_xpath('/html/body/form/input[1]')
# fname.send_keys("aks")
# lname = driver.find_element_by_xpath('/html/body/form/input[2]')
# lname.send_keys("kat")
# email = driver.find_element_by_xpath('/html/body/form/input[3]')
# email.send_keys("aks.kat@someemail.com")
fname = driver.find_element_by_name("fName")
lname = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
fname.send_keys("aksh")
lname.send_keys("kat")
email.send_keys("aksh.kat@someemail.com")
time.sleep(1)
submit_btn = driver.find_element_by_css_selector(".btn")
submit_btn.click()

time.sleep(5)
driver.quit()