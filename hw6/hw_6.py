# Задание 1
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number.

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

def index_in_range(arr, min_number, max_number):
    for i in range(0, len(arr)):
        if arr[i] in list(range(min_number, max_number+1)):
            print(i)

# index_in_range(list_1, min_number, max_number)

# Задача 2 
# Заполните массив элементами арифметической прогрессии. Её первый элемент a1 , разность d и количество элементов n будет задано автоматически. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

a1 = 2
d = 3
n = 4
def arif(a1, d, n):
    arr = []
    arr.append(a1)
    for i in range(2, n+1):
        arr.append(a1 + (i-1) * d)
    for i in arr:
        print(i)
arif(a1, d, n)