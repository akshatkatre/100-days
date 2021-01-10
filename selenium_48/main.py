from selenium import webdriver

URL = "https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_4?dchild=1&keywords=instant+pot&qid=1610190322&sr=8-4"
CHROME_DRIVER_PATH = "/Users/akshat/repo/chromedriver/chromedriver"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("https://www.python.org")
# search_bar = driver.find_element_by_name("q")
# print(search_bar)
#
# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)
#
# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)
#
# link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(link.text)
# price = driver.find_element_by_id("priceblock_ourprice")
# print(f"The price is: {price.text}")
# closes the tab that was opened by selenium
# driver.close()

events_dict = {}
time_links = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')
# print(time_links, type(time_links))
event_links = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')
print(len(time_links))
# counter = 0
for i in range(len(time_links)):
    events_dict[i] = {
        'time': time_links[i].text,
        'event': event_links[i].text
    }

print(events_dict)

event_links_new = driver.find_elements_by_css_selector(".event-widget li a")
for event in event_links_new:
    print(f"Event: {event.text}")
# quit the entire browser
driver.quit()
