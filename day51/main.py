import os
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/dmytrogrendach/my/Development/chromedriver"
TWITTER_EMAIL = "--your_email--"
TWITTER_PASSWORD = "--your_pass--"
URL = "https://fast.com"

class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
        self.upload = 0

    def get_internet_speed(self, url:str):
        self.driver.get(url)
        while (self.driver.current_url == url):
            pass
        self.upload = self.driver.find_element(By.CLASS_NAME, "speed-results-container succeeded").text
        self.driver.quit()
        print(f"Ping: {self.ping} ms")
        print(f"UP speed: {self.up} Mbps")
        print(f"Down speed: {self.down} Mbps")

    def tweet_at_proveder(self):
        print("Tweet")

    def tweet_at_provider(self):
        pass

speedtest = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
speedtest.get_internet_speed(URL)
