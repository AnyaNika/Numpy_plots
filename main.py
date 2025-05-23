import numpy as np
import matplotlib.pyplot as plt

# 1. Создай гистограмму для случайных данных, сгенерированных с помощью функции `numpy.random.normal`.
# # Параметры нормального распределения

mean = 0 # Среднее значение

std_dev = 1 # Стандартное отклонение

num_samples = 1000 # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

plt.hist(data, bins=15)

# Кастомизируем график:

plt.xlabel("Значение данных")
plt.ylabel("Количество данных")
plt.title("Гистограмма случайных данных")

# Показываем график:

plt.show()

# 2. Построй диаграмму рассеяния для двух наборов случайных данных,
# сгенерированных с помощью функции `numpy.random.rand`.

n = 10
random_array_x = np.random.rand(n) # массив из n случайных чисел
random_array_y = np.random.rand(n)
print(random_array_x, random_array_y)

plt.scatter(random_array_x, random_array_y)

plt.xlabel("Набор случайных данных X")
plt.ylabel("Набор случайных данных Y")
plt.title("Диаграмма рассеяния двух наборов случайных данных")

plt.show()