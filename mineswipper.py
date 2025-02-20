# Задача:
# Создайте игровое поле для "Сапёра" размером 10×10.
# Поле должно быть представлено в виде двумерного массива.
# Разместите 15 мин случайным образом (обозначьте их числом −1).
# Для каждой клетки без мины подсчитайте количество мин в соседних клетках.
# Визуализируйте:
# Само поле (где мины выделены красным).
# Поле с числами, где указано количество мин вокруг каждой клетки (для наглядности).
#

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

playboard = np.array([[1,0,1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1,0,1], [1,0,1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1,0,1] ,[1,0,1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1,0,1], [1,0,1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1,0,1]])
plt.imshow(playboard,cmap='hot')
plt.title('Сапер')
plt.xticks(range(10) , labels=[f'{i}' for i in range(1,11)])
plt.yticks(range(10),labels=[f'{i}' for i in range(1,11)])

# ax.text(1, 1, f'{int(6)}', ha='center', va='center', color='black', size = 20)
#plt.scatter(a1, b1, color='red', s=500)

d = 0
s = 0

# d = np.random.randint(1, 10, 15)
# s = np.random.randint(1, 10, 15)

zzz = np.random.choice(np.arange(0, 100), size=15, replace=False)

newx = np.array([])
newy = np.array([])

for i in zzz:
    s = i // 10
    newx = np.append(newx, s)
    d = i % 10
    newy = np.append(newy, d)
wwww = 0
# SSSSS = np.array([])
# for i in newx:
#     if i < 10:
#         wwww = i + 1
#         SSSSS = np.append(SSSSS, )

plt.scatter(newx, newy, color='red', s=500)

# gg = list(range(0,10))
#
# for i in gg:
#     ax.text(i, i, f'{int(6)}', ha='center', va='center', color='green', size = 20)
#
# plt.show()