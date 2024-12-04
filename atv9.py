from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# Utilizar o comando ¨source venv/bin/activate.fish" para ativar o ambiente virtual e rodar o selenium (n baixei globalmente para não causar conflitos)

driver = webdriver.Firefox()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
button.click()
    
alert = driver.switch_to.alert
print(f"Texto do alerta: {alert.text}")
alert.accept()

driver.quit()
