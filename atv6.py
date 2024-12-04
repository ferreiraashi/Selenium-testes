from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Utilizar o comando ¨source venv/bin/activate.fish" para ativar o ambiente virtual e rodar o selenium (n baixei globalmente para não causar conflitos)


driver = webdriver.Firefox()

driver.get("https://www.google.com")

search_bar = driver.find_element(By.NAME, "q")

search_bar.send_keys("Python Selenium")
search_bar.send_keys(Keys.RETURN)

driver.save_screenshot("resultado.png")

driver.quit()
