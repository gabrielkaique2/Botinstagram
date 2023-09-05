import requests
from bs4 import BeautifulSoup

# URL da página que você deseja fazer web scraping
url = 'https://www.youtube.com/watch?v=NS8DsXzU2Xg'

# Enviar uma solicitação GET para a página
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Analisar o conteúdo HTML da página com o Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extrair o título da página
    title = soup.title.string
    print(f'Título da página: {title}')
else:
    print('Falha ao acessar a página')