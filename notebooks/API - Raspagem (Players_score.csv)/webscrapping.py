# Esse arquivo pega todos os links dos jogos do Brasileirão até uma data específica. Essa raspagem é essencial, pois é através dela que teremos acesso às APIs. 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from datetime import datetime, timedelta
import time

# Função para gerar uma lista de datas entre 13 de abril de 2024 e 21 de setembro de 2024
# Essas datas serão usadas para construir as URLs de cada dia
def gerar_datas_2024():
    inicio = datetime(2024, 4, 13)  # Data de início da coleta de links
    fim = datetime(2024, 9, 21)     # Data final para a coleta de links
    delta = timedelta(days=1)       # Incremento diário
    datas = []
    data_atual = inicio
    # Gera a lista de datas no formato 'YYYY-MM-DD'
    while data_atual <= fim:
        datas.append(data_atual.strftime('%Y-%m-%d'))
        data_atual += delta
    return datas

# Configuração do WebDriver para o Chrome com modo "headless" (sem interface gráfica)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Executa o navegador sem abrir janelas
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Inicializa o driver do Chrome usando o gerenciador do WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Definimos a URL base do site da FIFA com filtros para jogos da Série A do Brasileirão
url_base = 'https://www.fifa.com/pt/match-centre?date={}&sortBy=Popular&term=Serie+A&idCompetition=2000000078'

# Gera a lista de datas de 2024, que serão inseridas na URL
datas_2024 = gerar_datas_2024()

# Lista para armazenar todos os links de jogos encontrados
todos_links_partidas = []

# Função que usa o Selenium para buscar os links das partidas de futebol em uma URL específica
def buscar_links_partidas_selenium(url):
    try:
        # Abre a URL no navegador
        driver.get(url)
        print(f"Carregando a página: {url}")
        
        # Espera até que todos os elementos de jogos estejam carregados na página (máximo 30 segundos)
        wait = WebDriverWait(driver, 30)
        jogos = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[href*="/pt/match-centre/match/2000000078/"]')))
        
        links_partidas = []
        # Para cada jogo encontrado, tenta obter o atributo 'href' (link)
        for jogo in jogos:
            try:
                href = jogo.get_attribute('href')  # Pega o link do jogo
                if href:
                    links_partidas.append(href)    # Adiciona o link à lista de links
            except StaleElementReferenceException:
                print("Elemento obsoleto, continuando para o próximo")
                continue
        
        return links_partidas
    except TimeoutException:
        print(f"Tempo limite excedido ao carregar a página {url}")  # Se a página não carregar no tempo limite
        return []
    except Exception as e:
        print(f"Erro ao buscar links na página {url}: {e}")  # Captura qualquer erro durante a execução
        return []

# Laço para percorrer todas as datas geradas
for data in datas_2024:
    url_data = url_base.format(data)  # Insere a data na URL base
    print(f"Acessando: {url_data}")
    
    # Busca os links das partidas para a data atual
    links_partidas = buscar_links_partidas_selenium(url_data)
    
    # Se encontrar links de jogos, adiciona à lista principal
    if links_partidas:
        todos_links_partidas.extend(links_partidas)
        print(f"Jogos encontrados para {data}: {len(links_partidas)} jogos")
    # Caso não encontre nenhum jogo para a data específica
    else:
        print(f"Nenhum jogo encontrado para a data {data}")
    
    # Pausa de 2 segundos entre as requisições para não sobrecarregar o servidor
    time.sleep(2)

# Após a coleta, exibe todos os links encontrados
if todos_links_partidas:
    print("\nLinks das partidas do Brasileirão 2024 encontrados:")
    for link in todos_links_partidas:
        print(link)
else:
    print("Nenhum link de partidas encontrado em todos os dias verificados.")

# Fecha o WebDriver ao final da execução
driver.quit()
