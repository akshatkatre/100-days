from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
from common import resource

tic = time.perf_counter()
URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
CHROME_DRIVER_PATH = "/Users/akshat/repo/chromedriver/chromedriver"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(url=URL)


def login():
    username = driver.find_element_by_css_selector("#username")
    username.send_keys(resource.get_resource_key("linkedin")['user'])
    password = driver.find_element_by_css_selector("#password")
    password.send_keys(resource.get_resource_key("linkedin")['pass'])
    submit_btn = driver.find_element_by_css_selector(".btn__primary--large")
    submit_btn.click()


sign_in = driver.find_element_by_link_text("Sign in")
sign_in.click()
time.sleep(3)

login()
time.sleep(3)

easy_apply_link = driver.find_element_by_css_selector('.job-card-container__apply-method')
easy_apply_link.click()

time.sleep(2)
easy_apply_submit_btn = driver.find_element_by_css_selector('.jobs-apply-button')
easy_apply_submit_btn.click()
time.sleep(2)
phone_num = driver.find_element_by_css_selector('.fb-single-line-text__input')
phone_num.send_keys(resource.get_resource_key("linkedin")['phone'])

toc = time.perf_counter()
print(f"elapsed time: {toc-tic}")
