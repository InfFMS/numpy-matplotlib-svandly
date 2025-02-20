# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.


import numpy as np
kubiki = np.random.randint(1,7,1000)

print(kubiki)

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0


for i in kubiki:
    if i == 1:
        one += 1
    if i == 2:
        two += 1
    if i == 3:
        three += 1
    if i == 4:
        four += 1
    if i == 5:
        five += 1
    if i == 6:
        six += 1

print(one, two, three, four, five, six)

odin = one / 1000
dva = two / 1000
tri = three / 1000
chetire = four / 1000
piat = five / 1000
shest = six / 1000

max = 0
utiputi = 0

for i in kubiki:
    if kubiki[i] == kubiki[i + 1]:
        max += 1
    else:
        if max > utiputi:
            utiputi = max
            max = 0

print(utiputi)
# print(max)

import matplotlib.pyplot as plt

x1 = list(range(1,7))
y1 = [one, two, three, four, five, six]

plt.bar(x1, y1, color = 'blue')
plt.title("Выпадение кубика")
plt.show()