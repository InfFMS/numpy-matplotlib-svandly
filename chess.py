# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.


import numpy as np
import matplotlib.pyplot as plt

print('Введите координату по Х и Y')

a = int(input())
b = int(input())

positions = [a - 1, b - 1]

n = 0
m = 0
a1 = a
b1 = b

fig, ax = plt.subplots()

pole = np.array([[1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1], [1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1] ,[1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1]])
plt.imshow(pole, cmap = 'hot')
plt.title("Шахматы")
plt.xticks(range(8), labels=[f'{i}' for i in range(1,9)])
plt.yticks(range(8), labels=[f'{i}' for i in range(1,9)])


while n < 8:
    plt.scatter(a-1, n, color='red', s=500)
    n+=1
while m < 8:
    plt.scatter(m, b-1, color='red', s=500)
    m+=1
while (a1 < 8) and (b1 < 8):
    plt.scatter(a1, b1, color='red', s=500)
    a1 += 1
    b1 += 1

a1 = a
b1 = b

while (a1 > -1) and (b1 > -1):
    plt.scatter(a1, b1, color='red', s=500)
    a1 -= 1
    b1 -= 1

a1 = a
b1 = b - 2


while (a1 < 8) and (b1 > -1):
    plt.scatter(a1, b1, color='red', s=500)
    a1 += 1
    b1 -= 1

a1 = a - 2
b1 = b

while (a1 > -1) and (b1 < 8):
    plt.scatter(a1, b1, color='red', s=500)
    a1 -= 1
    b1 += 1


plt.scatter(a-1, b-1, color='green', s=1000)
plt.show()