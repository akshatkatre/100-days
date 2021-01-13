import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from common import resource

CHROME_DRIVER_PATH = "/Users/akshat/repo/chromedriver/chromedriver"
URL = "https://www.instagram.com/"
SIMILAR_ACCOUNT = "chefsteps"
INSTA_USER = resource.get_resource_key('instagram')['user']
INSTA_PASS = resource.get_resource_key('instagram')['pass']


class InstaFollower:

    def __init__(self):
        self.driver = self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        """
        This function will log into instagram
        :return:
        """
        print('logging into Instagram')
        self.driver.get(URL)
        time.sleep(2)
        username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(INSTA_USER)

        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(INSTA_PASS)

        submit_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        submit_button.click()
        print('login complete...')

    def find_followers(self):
        """
        This function will search for SIMILAR_ACCOUNT to find followers
        :return:
        """
        int_btn_1 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        int_btn_1.click()
        print('Intermediate button 1 clicked...')
        time.sleep(2)

        int_btn_2 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        int_btn_2.click()
        print('Intermediate button 2 clicked...')
        time.sleep(2)

        search_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_box.send_keys(SIMILAR_ACCOUNT)
        search_box.send_keys(Keys.ENTER)
        print(f'Searching for {SIMILAR_ACCOUNT}...')
        time.sleep( 2)

        search_box_1 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]/div/div[2]/div/span')
        search_box_1.click()
        print(f'{SIMILAR_ACCOUNT} clicked')
        time.sleep(2)

        followers_link = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_link.click()
        print(f'followers for {SIMILAR_ACCOUNT} clicked...')

    def follow(self):
        """
        This function will get list of all followers for the similar account
        and follow.
        :return:
        """
        print('Inside follow...')
        dialog = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(1, 10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
            time.sleep(random.randint(500, 1000) / 1000)
            try:
                followers_name =self.driver.find_elements_by_css_selector('.wFPL8')
                for follower_name in followers_name:
                    print(follower_name.text)
            except NoSuchElementException:
                print('Not found...')
            except StaleElementReferenceException:
                print('Nof found...')

        print('Inside follow complete...')


insta_bot = InstaFollower()
insta_bot.login()
time.sleep(5)
insta_bot.find_followers()
time.sleep(2)
insta_bot.follow()