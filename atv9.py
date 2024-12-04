from selenium import webdriver
from selenium.webdriver.common.alert import Alert

# Utilizar o comando ¨source venv/bin/activate.fish" para ativar o ambiente virtual e rodar o selenium (n baixei globalmente para não causar conflitos)

driver = webdriver.Chrome()

driver.get("https://example.com")

# Lidar com o alerta
alert = Alert(driver)
alert.accept()  # Para fechar o alerta

driver.quit()
