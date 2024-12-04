from selenium import webdriver
from selenium.webdriver.common.by import By

# Utilizar o comando ¨source venv/bin/activate.fish" para ativar o ambiente virtual e rodar o selenium (n baixei globalmente para não causar conflitos)

driver = webdriver.Firefox()

driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

success_message = driver.find_element(By.CLASS_NAME, "flash").text
if "You logged into a secure area!" in success_message:
    print("Login bem-sucedido!")

driver.quit()
