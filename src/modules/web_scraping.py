"""
+ Web Scraping com Python usando requests e bs4 BeautifulSoup
- Web Scraping é o ato de "raspar a web" buscando informações de forma
automatizada, com determinada linguagem de programação, para uso posterior.
- O módulo requests consegue carregar dados da Internet para dentro do seu
código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
em formato de objetos Python para facilitar a vida do desenvolvedor.
- Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
+ Instalação
- pip install requests types-requests bs4
"""

import re

import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:3333'

response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')
# print(raw_html)

print(parsed_html)
print(parsed_html.title)
if parsed_html.title:
	print(parsed_html.title.text)

top_jobs_header = parsed_html.select_one('#intro > div > div > article > h2')

print(top_jobs_header)
if top_jobs_header:
	print(top_jobs_header.text)
	article = top_jobs_header.parent

	if article:
		print(article.text)

		for p in article.select('p'):
			print(re.sub(r'\s{1,}', '', p.text).strip())
