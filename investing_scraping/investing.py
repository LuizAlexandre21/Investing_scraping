# Pacotes
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 
import random
import time 
from selenium.webdriver.common.by import By
import shutil
from selenium.webdriver.chrome.options import Options

# Abrindo o navegador 
def open_chrome(download_path:str):
    # Definindo opções do chrome 
    chrome_options = Options()

    # Configurando as opções do chrome 
    # Removendo Sandboxs 
    chrome_options.add_argument("--no-sandbox")

    # Removendo shm 
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Desativando o uso de gpu 
    #chrome_options.add_argument("--disable-gpu")

    # Deixando o navegador em segundo plano 
    # chrome_options.add_argument("--headless")

    # Desativando o bloqueio de popups 
    chrome_options.add_argument("--disable-popup-blocking")

    # Desativando as notificações 
    chrome_options.add_argument("--disable-notifications")

    # Adicionando a pagina de download nas preferencias 
    prefs = {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
    }
    chrome_options.add_experimental_option("prefs", prefs)
    # Retorna o navegador aberto

    # Importando o webdrive chrome 
    chrome = webdriver.Chrome('chrome/chromedriver',options=chrome_options)

    return chrome

# Logando no site do investing 
def investing_login(email:str,password:str):

    # Abrindo o navegador 
    navegador = open_chrome('/home/alexandre/Documents/ADECE/Investing/Data/')

    # Acessando o site do investing 
    navegador.get("https://br.investing.com/rates-bonds/u.s.-2-year-bond-yield-historical-data")

    # Interromper o carregamento da pagina 
    navegador.execute_script("window.stop();")

    # Removendo a aba de cookies
    navegador.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[2]/button').click()

    # Acessando a aba de login
    navegador.find_element(By.XPATH,'//*[@id="__next"]/header/div[1]/section/div[3]/ul/li[1]/button').click()

    # Acessando o login com conta do investing 
    navegador.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/form/button[3]').click()

    # Inserindo o email 
    navegador.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/form/div[3]/input').send_keys(email)

    # Inserindo a Senha 
    navegador.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/form/div[5]/input').send_keys(password)

    # Logando a conta 
    navegador.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/form/button').click()

    return navegador