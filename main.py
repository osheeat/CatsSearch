import requests
from bs4 import BeautifulSoup
import os

# URL страницы Википедии
search_str = 'кошка'
url = 'https://ru.wikipedia.org/wiki/' + search_str

# Отправляем GET-запрос и получаем содержимое страницы
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Создаем папку для сохранения фотографий
os.makedirs('images', exist_ok=True)

# Ищем все теги img на странице
image_tags = soup.find_all('img')

# Скачиваем и сохраняем изображения
for tag in image_tags:
    image_url = tag['src']
    if image_url.startswith('//'):
        image_url = 'https:' + image_url
    elif not image_url.startswith('http'):
        image_url = url + image_url

    response = requests.get(image_url)

    filename = os.path.join('images', os.path.basename(image_url))
    with open(filename, 'wb') as file:
        file.write(response.content)

print('Изображения сохранены в папке "images"')