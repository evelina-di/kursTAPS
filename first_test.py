from selenium import webdriver

import time

driver = webdriver.Chrome("/Users/dikta/OneDrive/Dokumenty/Chrome Webdriver/chromedriver.exe")

driver.get('https://google.pl')

zgadzam_sie = driver.find_element_by_id("L2AGLb")

zgadzam_sie.click()

search_box = driver.find_element_by_name('q')

search_box.send_keys('selenium python')

search_box.submit()

time.sleep(5)

driver.quit()