from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://www.selenium.dev/")

downloads_link = driver.find_element(By.LINK_TEXT, "Downloads")
downloads_link.click()

header = driver.find_element(By.TAG_NAME, "h1")
print("Texto do cabeçalho:", header.text)

driver.quit()
