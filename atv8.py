from selenium import webdriver
from selenium.webdriver.common.by import By

# Utilizar o comando ¨source venv/bin/activate.fish" para ativar o ambiente virtual e rodar o selenium (n baixei globalmente para não causar conflitos)

driver = webdriver.Firefox()

driver.get("https://www.selenium.dev/")

downloads_link = driver.find_element(By.LINK_TEXT, "Downloads")
downloads_link.click()

header = driver.find_element(By.TAG_NAME, "h1")
print("Texto do cabeçalho:", header.text)

driver.quit()
