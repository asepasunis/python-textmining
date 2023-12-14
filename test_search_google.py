import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://www.google.com')
search = browser.find_element(By.NAME, "q")
search.clear()
search.send_keys("Asep Abdul Sofyan")
search.send_keys(Keys.RETURN)  # hit return after you enter search text
titles = browser.find_elements(By.CLASS_NAME, "yuRUbf")
for title in titles:
    print(title.text.encode("utf8"))
time.sleep(10)
browser.quit()
