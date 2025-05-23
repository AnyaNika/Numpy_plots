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
     divan_price = divan.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH').text
   except Exception as e:
     print(f"произошла ошибка при парсинге: {e}")
     continue

    # Вносим найденную информацию в список
   parsed_data.append([divan_price])

# Закрываем подключение браузер
driver.quit()

# Прописываем открытие нового файла, задаём ему название и форматирование
# 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
with open("divan.csv", 'w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Цена'])
    writer.writerows(parsed_data)


def clean_price(price):
    # Удаляем "руб." и преобразуем в число
    return int(price.replace('руб.', '').replace(' ', ''))


# Чтение данных из исходного CSV файла и их обработка
input_file = 'divan.csv'
output_file = 'cleaned_prices.csv'

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='',
                                                                  encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Читаем заголовок и записываем его в новый файл
    header = next(reader)
    writer.writerow(header)

    # Обрабатываем и записываем данные строк
    for row in reader:
        clean_row = [clean_price(row[0])]
        writer.writerow(clean_row)

print(f"Обработанные данные сохранены в файл {output_file}")

