from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time

URL = "http://orteil.dashnet.org/experiments/cookie/"
CHROME_DRIVER_PATH = "/Users/akshat/repo/chromedriver/chromedriver"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(url=URL)


def purchase(m_value: int):
    # buy_portal = driver.find_element_by_xpath('//*[@id="buyPortal"]/b')
    # buy_portal_value = int(buy_portal.text.replace(',', '').split(' - ')[1])
    # print(f"buy portal: {buy_portal_value}")
    # if m_value > buy_portal_value:
    #     buy_portal.click()
    #     return True
    #
    # buy_alchemy = driver.find_element_by_xpath('//*[@id="buyAlchemy lab"]/b')
    # buy_alchemy_value = int(buy_alchemy.text.replace(',', '').split(' - ')[1])
    # print(f"buy alchemy: {buy_alchemy_value}")
    # if m_value > buy_alchemy_value:
    #     buy_alchemy.click()
    #     return True

    buy_shipment = driver.find_element_by_xpath('//*[@id="buyShipment"]/b')
    buy_shipment_value = int(buy_shipment.text.replace(',','').split(' - ')[1])
    print(f"buy shipment: {buy_shipment_value}")
    if m_value > buy_shipment_value:
        buy_shipment.click()
        return True

    buy_mine = driver.find_element_by_xpath('//*[@id="buyMine"]/b')
    buy_mine_value = int(buy_mine.text.replace(',','').split(' - ')[1])
    print(f"buy mine: {buy_mine_value}")
    if m_value > buy_mine_value:
        buy_mine.click()
        return True

    buy_factory = driver.find_element_by_xpath('//*[@id="buyFactory"]/b')
    buy_factory_value = int(buy_factory.text.split(' - ')[1])
    print(f"buy factory: {buy_factory_value}")
    if m_value > buy_factory_value:
        buy_factory.click()
        return True

    buy_grandma = driver.find_element_by_xpath('//*[@id="buyGrandma"]/b')
    buy_grandma_value = int(buy_grandma.text.split(' - ')[1])
    print(f"buy grandma: {buy_grandma_value}")
    if m_value > buy_grandma_value:
        buy_grandma.click()
        return True

    buy_cursor = driver.find_element_by_xpath('//*[@id="buyCursor"]/b')
    buy_cursor_value = int(buy_cursor.text.split(' - ')[1])
    print(f"buy cursor: {buy_cursor_value}")
    if m_value > buy_cursor_value:
        buy_cursor.click()
        return True

    return False

cookie = driver.find_element_by_css_selector("#cookie")
game_on = True

game_start_time = datetime.now()
while game_on:
    cookie.click()
    money = driver.find_element_by_css_selector("#money")
    money_value = int(money.text)
    current_time = datetime.now()
    delta = current_time - game_start_time
    if delta.seconds > 300:
        game_on = False
    if delta.seconds % 5 == 0:
        print(f"seconds elapsed: {delta.seconds}; money: {money_value}")
        purchase(money_value)

print("Game ended..")



# if seconds elapsed is greater than 300 seconds (5 minutes) then end program
# if seconds % 5 then



