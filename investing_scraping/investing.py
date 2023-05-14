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