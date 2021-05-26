from selenium import webdriver

driver = webdriver.Chrome("/Users/dikta/OneDrive/Dokumenty/Chrome Webdriver/chromedriver.exe")

driver.get("https://fabrykatestow.pl")
driver.maximize_window()
kursy = driver.find_element_by_xpath("/html/body/div[1]/header/div/nav[1]/div/div/div/div[2]/div/div/div/ul/li[2]/a")
kursy.click()

kursTAPS = driver.find_element_by_xpath("/html/body/div[1]/main/div/div/div/section/div[2]/div/div/div/div/section[1]/div/div/div[1]/div/div/div/div/div/a/span/span[2]")
kursTAPS.click()

instr = driver.find_element_by_css_selector("#content > div > div > div > div > div > div > div > section.elementor-section.elementor-top-section.elementor-element.elementor-element-ee27147.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default > div.elementor-container.elementor-column-gap-default")
scroll = instr.location_once_scrolled_into_view

driver.save_screenshot("zdjeciePawla.png")

driver.close()