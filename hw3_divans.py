# 3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю цену и вывести ее,
# а также сделать гистограмму цен на диваны.

from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome()

url = "https://www.divan.ru/category/divany-i-kresla"

# Открываем веб-страницу
driver.get(url)

# Находим все карточки с диванами
divans = driver.find_elements(By.CLASS_NAME, 'lsooF')
print(divans)

# Создаём список, в который потом всё будет сохраняться
parsed_data = []

# Перебираем коллекцию диванов

for divan in divans:
   try:
     # Находим цену
     price = divan.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH').text
   except Exception as e:
     print(f"произошла ошибка при парсинге: {e}")
     continue

    # Вносим найденную информацию в список
   parsed_data.append([price])

# Закрываем подключение браузер
driver.quit()

# Прописываем открытие нового файла, задаём ему название и форматирование
# 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
with open("divan.csv", 'w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Цена'])
    writer.writerows(parsed_data)

