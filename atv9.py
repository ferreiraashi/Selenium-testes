from selenium import webdriver
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()

driver.get("https://example.com")

# Lidar com o alerta
alert = Alert(driver)
alert.accept()  # Para fechar o alerta

driver.quit()
