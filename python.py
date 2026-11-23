import random


# ТУТ ЗАДАНИЕ 1
while True:
    try:
        n = int(input("Введите размер N: ")) # rows
        m = int(input("Введите размер M: ")) # columns
        break
    except ValueError:
        print("Размер должен быть интом!!!!")

a = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(1, 99))
    a.append(row)
print("Исходная матрица:")
for row in a:
    print(row)


for i in range(n):
    for j in range(n - 1):
        if min(a[j]) > min(a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]
print("Отсортированная матрица:")
for row in a:
    print(row)


# ТУТ ЗАДАНИЕ 2
s = input("Введите последовательность чисел: ")

d = {}

for c in s:
    if c.isdigit() and 0 <= int(c) <= 9:
        if int(c) in d:
            d[int(c)] += 1
        else:
            d[int(c)] = 1
print("Словарь: ", d)

while True:
    try:
        x = int(input("Введите цифру для поиска: "))
        break
    except ValueError:
        print("Введите цифру!")

if x in d:
    print("Кол-во повторений: ", d[x])
else:
    print("Цифры нет")