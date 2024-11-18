

#############################################################
### use this file to implement the web scrapper in part 1 ###
#############################################################


import requests as rq
from bs4 import BeautifulSoup as bs
from selenium import webdriver as se
from selenium.webdriver.common.by import By
import time

#URL = "https://www.rit.edu/dubai/directory"

#page = rq.get(URL)

#soup = bs(page.text, "html.parser")

driver = se.Chrome()

driver.get("https://www.rit.edu/dubai/directory")

#for loop to click 'load more' 5 times
for i in range(5):
        button = driver.find_element(By.CLASS_NAME,"see-more") #selecting the element from its class
        driver.execute_script("arguments[0].scrollIntoView(true);", button) #scrolls to element so that it can be clickable (doesnt work without this for sum reason)
        button.click()
        time.sleep(5) #waits for 5 seconds to give the page time to load

input("enter to exit") #for now.. testing purposes only :3
driver.quit()
