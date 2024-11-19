

#############################################################
### use this file to implement the web scrapper in part 1 ###
#############################################################


import requests as rq
from bs4 import BeautifulSoup as bs
from selenium import webdriver as se
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = se.Chrome()

driver.get("https://www.rit.edu/dubai/directory")

#for loop to click 'load more' 5 times
for i in range(5):
        button = driver.find_element(By.CLASS_NAME,"see-more") #selecting the element from its class
        driver.execute_script("arguments[0].scrollIntoView(true);", button) #scrolls to element so that it can be clickable (doesnt work without this for sum reason)
        button.click()
        time.sleep(3) #waits for 5 seconds to give the page time to load


soup = bs(driver.page_source, "html.parser") #to extract html code of the webpage
driver.quit()
#problem is that we need to use requests module 


#seconmd problem find way to parse
employee = soup.select(".pb-2")  # Extracting all lines
data = [e.get_text(strip=True) for e in employee]  # Clean text

# Group the lines into sets of four (Name, Title, Workplace, Email)
structured_data = []
for i in range(0, len(data)):  # Process every 4 lines
    if i + 3 < len(data):  # Ensure there are enough lines for a complete record
        name = data[i]
        title = data[i + 1]
        # Skipping workplace line (data[i + 2]) as it's not needed
        email = data[i + 3]
        structured_data.append([name, title, email])

# Create a DataFrame
df = pd.DataFrame(structured_data, columns=["Name", "Title", "Email"])

# Save to CSV
df.to_csv("directory.csv", index=False)

