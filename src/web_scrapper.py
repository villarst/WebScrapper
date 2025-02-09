import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class WebScrapper:
    def __init__(self):
        self.service = Service(executable_path="driver_executable\chromedriver.exe")
        self.driver = webdriver.Chrome(service = self.service)
        
    def run_driver(self):
        self.driver.get("https://google.com")
        time.sleep(2)
        self.driver.quit()
