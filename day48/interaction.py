from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/dmytrogrendach/my/Development/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element("css selector", "#articlecount a")
article_count.click()

pages = driver.find_element("link text", "Pages")
pages.click()

search = driver.find_element("name","search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
