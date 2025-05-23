import pandas as pd
import matplotlib.pyplot as plt



# Загрузка данных из CSV-файла
file_path = 'cleaned_prices.csv'
data = pd.read_csv(file_path)

prices = data['Цена']
mean_price = prices.mean()
print(f'Средняя цена на диван - {mean_price} руб.')
plt.hist(prices, bins=10, edgecolor='blue')

plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена')
plt.ylabel('Частота')

plt.show()