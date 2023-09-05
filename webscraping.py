import requests
from bs4 import BeautifulSoup

# URL da página que você deseja fazer web scraping
url = 'https://www.instagram.com/crisiane_melissas/following/'

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

# Enviar uma solicitação GET para a página
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Analisar o conteúdo HTML da página com o Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extrair o título da página
    title = soup.title.string
    #print(f'Título da página: {title}')

    fallowers = soup.find_all('div', class_="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1pi30zi x1swvt13 xwib8y2 x1y1aw1k x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1")
    print(fallowers)
else:
    print('Falha ao acessar a página')

requisicao = requests.get(url, headers=headers)

print(requisicao)