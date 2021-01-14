import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

CHROME_DRIVER_PATH = "/Users/akshat/repo/chromedriver/chromedriver"
ZILLOW_URL = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
FORMS_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSfrQ14K59TciFvTVC6a9CaXQN3qGNhsow4wwHLEW6uzWoWkLw/viewform?usp=sf_link'


def get_static_contents(file_name: str) -> str:
    with open(file_name, 'r') as file_handle:
        return file_handle.read()


def store_static_contents(file_name: str, contents: str):
    with open(file_name, 'w') as file_handle:
        file_handle.write(contents)


def get_zillow_data():
    """
    Use beautiful soup to scrape data from the Zillow website.
    For each apartment the Price, Address and Link will be scraped and
    added to a list object.
    The list object will be returned
    :return:
    list[str]: List of dictionary will be returned
    """
    # Adding headers to avoid captcha
    headers = {
        "User-Agent": "en-US,en;q=0.5",
        "Accept-Language": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0"
    }

    # Get html contents dynamically
    contents = requests.get(url=ZILLOW_URL, headers=headers).text

    # Get html contents statically - For testing
    # contents: str = get_static_contents('data.html')

    soup = BeautifulSoup(contents, "html.parser")
    data = []
    # print(soup.prettify())

    all_prices = soup.find_all(class_='list-card-price')
    all_addresses = soup.find_all(class_='list-card-addr')
    all_links = soup.find_all(class_="list-card-link")

    ZILLOW_TEXT = 'https://www.zillow.com'

    for counter in range(len(all_prices)):
        link_str = all_links[counter]['href']
        if ZILLOW_TEXT not in link_str:
            link_str = ZILLOW_TEXT + link_str
        data.append({
            'address': all_addresses[counter].getText(),
            'price': all_prices[counter].getText().split(' ')[0].replace('/mo', '').replace('+', ''),
            'link': link_str
        })
    # print(data)
    return data


def fill_google_form(data):
    """
    Open the google form URL.
    for each property as part of list, input the data into the form.
    :param data: List data that is used to fill google form
    :return:
    """
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    driver.get(url=FORMS_URL)
    time.sleep(2)
    for row in data:
        # print(row['price'], row['address'], row['link'])
        try:
            address_input = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address_input.send_keys(row['address'])
            price_input = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_input.send_keys(row['price'])
            link_input = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input.send_keys(row['link'])
            submit_btn = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
            submit_btn.click()
            time.sleep(1)

            submit_another = driver.find_element_by_link_text('Submit another response')
            submit_another.click()
            print(row['price'], row['address'], row['link'])
            time.sleep(1)
        except NoSuchElementException:
            print('Exception occurred...')

    driver.quit()


rental_data = get_zillow_data()
fill_google_form(rental_data)
