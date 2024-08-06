import requests
import csv
from bs4 import BeautifulSoup

page = requests.get('https://cookpad.com/ec/buscar/resetas')

soup = BeautifulSoup(page.text, 'html.parser')

f = csv.writer(open('resetas.csv', 'w'))
f.writerow(['Autor', 'Categoria', 'Frase'])

blockquote_items = soup.find_all('blockquote')

for blockquote in blockquote_items:
    titulo = blockquote.find(class_='block-link__main').text
    ingresdientes = blockquote.find(class_='inline-block px-xs text-cookpad-gray-400').text
    frase = blockquote.find('q').text

    f.writerow([titulo, ingresdientes, frase])
