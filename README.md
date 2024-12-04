Parte 1: Questões Teóricas

1. Diferença entre Selenium IDE e Selenium WebDriver:

    Selenium IDE:
    É uma ferramenta simples para gravar e reproduzir testes diretamente no navegador. Ideal para iniciantes e prototipagem rápida, mas possui funcionalidades limitadas.
    Selenium WebDriver:
    É uma API mais robusta e flexível que permite criar scripts de teste em várias linguagens (Python, Java, etc.). É usada para automação avançada e testes complexos.

2. Principais tipos de localizadores (locators):

    ID: Busca elementos pelo valor único do atributo id.
    Exemplo: driver.find_element(By.ID, "element_id").
    XPATH: Busca elementos usando expressões XPath.
    Exemplo: driver.find_element(By.XPATH, "//div[@class='class_name']").

3. O que é um WebElement no Selenium?
Um WebElement representa um elemento na página da web que pode ser interagido (clicar, enviar texto, etc.).
Exemplo:

search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("Python Selenium")

4. Interação com elemento não visível ou carregado:
O Selenium levanta um erro NoSuchElementException. Para resolver, use o comando WebDriverWait com condições explícitas:

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "element_id"))
)

5. Limitações do Selenium IDE:

    Não suporta integração com linguagens de programação, limitando a automação avançada.
    Não é adequado para testes complexos ou projetos que requerem gerenciamento de dados.
