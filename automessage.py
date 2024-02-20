from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Configuração do serviço do Chrome
servico = Service(ChromeDriverManager().install())

# Inicialização do navegador
driver = webdriver.Chrome(service=servico)

# URL para acessar o Google Messages
url = 'https://messages.google.com/web/conversations'

# Acessar a URL e esperar o carregamento da página
driver.get(url)
time.sleep(20)

# Clicar em uma conversa específica (exemplo: a primeira da lista)
url_conversa = 'https://messages.google.com/web/conversations/190'
driver.get(url_conversa)
time.sleep(10)

# Capturar elementos e imprimir seus textos
get_click_btn = driver.find_elements(By.CLASS_NAME, 'ng-star-inserted')
for click in get_click_btn:
    print(click.text)

# Abrir uma nova conversa
url_nova_conversa = 'https://messages.google.com/web/conversations/new'
driver.get(url_nova_conversa)
time.sleep(5)

# Digitar o número do destinatário
campo_numero = driver.find_element(By.TAG_NAME, 'input')
campo_numero.send_keys('842289861')
time.sleep(5)

# Clicar para selecionar o contato
click_contato = driver.find_element(By.CLASS_NAME, 'anon-contact-name')
click_contato.click()
time.sleep(5)

# Voltar para a conversa anterior
driver.get(url_conversa)
time.sleep(5)

# Digitar e enviar a mensagem automatizada
campo_mensagem = driver.find_element(By.TAG_NAME, 'input')
campo_mensagem.send_keys('SMS AUTOMATIZADO ENVIADO COM SUCESSO!')
campo_mensagem.click()
time.sleep(5)

# Clicar para enviar a mensagem
click_enviar = driver.find_element(By.CLASS_NAME, 'ng-star-inserted')
click_enviar.click()
time.sleep(5)

# Fechar o navegador
driver.quit()
