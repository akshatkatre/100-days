from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from common import resource

PROMISED_DOWN: float = 150
PROMISED_UP: float = 10
CHROME_DRIVER_PATH = "/Users/akshat/repo/chromedriver/chromedriver"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.promised_down = PROMISED_DOWN
        self.promised_up = PROMISED_UP
        self.twitter_user = resource.get_resource_key('twitter')['user']
        self.twitter_pass = resource.get_resource_key('twitter')['pass']
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.url_speed_test = "https://www.speedtest.net/"

    def get_internet_speed(self):
        """
        The function will check the internet speed and using selenium and get
        the upload and download speed.
        If the upload or download speed are less the the predetermined amounts,
        then the invoke the method tweet_at_provider
        :return:
        """
        self.driver.get(url=self.url_speed_test)
        time.sleep(10)

        go_button = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()

        print("sleeping for 60 seconds")
        time.sleep(60)
        print("waking up...")

        download_speed = self.driver.find_element_by_css_selector('.download-speed').text
        print(f"download speed {download_speed}")

        upload_speed = self.driver.find_element_by_css_selector('.upload-speed').text
        print(f"upload speed {upload_speed}")

        if float(download_speed) < self.promised_down or float(upload_speed) < self.promised_up:
            message = f"Hey Internet Provider, why is my internet speed" \
                      f"{download_speed}down/{upload_speed}up when i pay " \
                      f"{self.promised_down}/down and {self.promised_up}up?"
            print(message)
            # Send a tweet
            self.tweet_at_provider(message)

    def tweet_at_provider(self, tweet: str):
        """
        The method will take a tweet string message, invoke the twitter login
        screen, after loggin into twitter, the tweet string will be pasted into
        the tweet text input.
        :param tweet: message that needs to be tweeted.
        :return:
        """
        twitter_url = "https://twitter.com/login/"
        self.driver.get(url=twitter_url)

        username = self.driver.find_element_by_name("session[username_or_email]")
        username.send_keys(self.twitter_user)

        password = self.driver.find_element_by_name("session[password]")
        password.send_keys(self.twitter_pass)

        login_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        login_button.click()

        time.sleep(10)
        try:
            tweet_text_area = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
            tweet_text_area.send_keys(tweet)
        except NoSuchElementException:
            print('Element not found...')


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
# bot.tweet_at_provider("hey the message goes here...")
