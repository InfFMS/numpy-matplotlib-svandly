# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.

import numpy as np

random_integers = np.random.randint(-10, 36, size=(365))
print(random_integers)
d = []

for i in random_integers:
    if i > -1:
        d.append(i)
    else:
        d.append(0)
massiv = np.array(d)



m = 0
i = 0
for i in random_integers:
    m = m + i
print(m/365)

i = 0
num = 0

x_1, y_1 = np.unique(random_integers, return_counts=True)


for i in random_integers:
    if i > 25:
        num += 1
print(num)



i = 0
n = 0
max = 0

for i in random_integers:
    if i < 0:
        n += 1
    if i > -1:
        if n > max:
            max = n
        n = 0
print(max)


import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 6))

# x_1 = np.linspace(1,366,365)
x = list(range(1,366))
y = random_integers


plt.plot(x, y)
plt.plot(x, massiv, color='red')
plt.title("График погоды")
plt.xlabel("Дни")
plt.ylabel("Погода")
plt.show()


plt.bar(x_1, y_1, color='blue')
plt.title("Диаграмма погоды")
plt.show()
