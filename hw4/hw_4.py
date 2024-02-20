# Задача 1
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо
var1 = '5 4' 
var2 = '10 1 3 5 7 9 1 1 1' 
var3 = '2 3 4 5 4 2 2' 


def to_find_copies(nums_str1, nums_str2):
    nums_str1 = set(list(map(lambda x: int(x), nums_str1.split())))
    nums_str2 = set(list(map(lambda x: int(x), nums_str2.split())))
    # nums_str1 = set(nums_str1) # попытка 2 не работает с 10 20 и т.д.
    # nums_str2 = set(nums_str2)
    # return sorted(nums_str1.intersection(nums_str2))
    return sorted(nums_str1 & nums_str2)
print(*to_find_copies(var2, var3))


# Задача 2
# В фермерском хозяйстве в Карелии выращивают чернику. Черника растет на круглой грядке, и кусты черники высажены по окружности грядки. Каждый куст черники имеет урожайность, которая соответствует количеству ягод на этом кусте.

# Урожайность черничных кустов представлена в виде списка arr, где arr[i] - это урожайность (количество ягод) i-го куста.

# В фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Каждый собирающий модуль может собрать ягоды с одного куста и с двух соседних кустов. Собирающий модуль находится перед определенным кустом, и он может выбирать, с какого куста начать сбор ягод.

# Ваша задача - написать программу, которая определит максимальное число ягод, которое может собрать один собирающий модуль за один заход, находясь перед некоторым кустом грядки.

# Входные данные:

# На вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го куста черники. Размер списка не превышает 1000 элементов.

# Выходные данные:

# Программа должна вывести одно целое число - максимальное количество ягод, которое может собрать собирающий модуль, находясь перед некоторым кустом грядки.
arr = [5, 8, 6, 4, 9, 2, 7, 3]  # 19

def to_find_best (arr):
    max = 0
    for i in range(1, len(arr)-1):
        if (arr[i-1] + arr[i] + arr[i+1]) > max:
            max = arr[i-1] + arr[i] + arr[i+1]
    return max
print(to_find_best(arr))