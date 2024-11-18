

#############################################################
### use this file to implement the web scrapper in part 1 ###
#############################################################


import requests as rq
from bs4 import BeautifulSoup as bs
from selenium import webdriver as se
from selenium.webdriver.common.by import By

#URL = "https://www.rit.edu/dubai/directory"

#page = rq.get(URL)

#soup = bs(page.text, "html.parser")


driver = se.Chrome()

driver.get("https://www.rit.edu/dubai/directory")

button = driver.find_element(By.CSS_SELECTOR,"see-more")

button.click()
