#Задача №9. По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

"""
n = int(input())
f = 1

while n > 0:
    f = f * n       # f *= n
    n = n - 1       # n -= 1
print(f)
"""
# второй вариант
"""
n = int(input())
f = 1
for i in range(2, n + 1):
    f *= i
print(f)
"""

# Задача №11. Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть выведите такое число n, 
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
"""
A = int(input())
f1 = 0
f2 = 1
i = 2

while f2 < A:
    f1, f2 = f2, f1 + f2
    i += 1

if A != f2:    
    i = -1
print(i)
"""

# Задача №13. Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
# В следующих строках располагается N целых чисел. Каждое число – 
# среднесуточная температура в соответствующий день. Температуры – 
# целые числа и лежат в диапазоне от –50 до 50.

"""
n = int(input('Введите количество дней: '))
k = 0
maximum = 0

for i in range(n):
    temp = int(input('Ведите значение температуры: '))
    if temp >= 0:
        k += 1
        if k > maximum:
            maximum = k    # maximum = max(maximum, k)
    else:
        k = 0
print(f"Максимальная оттепель составляет {maximum} дня.")
"""

#Задача №15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, 
# а для тещи полегче. Но вот незадача: арбузов слишком 
# много и он не знает как же выбрать самый легкий и самый 
# тяжелый арбуз? Помогите ему! 
# Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой строчке
# каждое. Здесь каждое число – это масса соответствующего арбуза.
"""  1 вариант:
n = int(input('Введите количество арбузов: '))

minimum = 100000000
maximum = 0
for i in range(n):
    weight = int(input('Введите массу арбуза: '))
    if weight > maximum:
        maximum = weight
    if weight < minimum:
        minimum = weight
print(minimum, maximum)   
"""

"""  2 вариант:
n = int(input('Введите количество арбузов: '))
weight = int(input('Введите массу арбуза: '))
minimum = weight
maximum = weight
for i in range(n-1):
    weight = int(input('Введите массу арбуза: '))
    if weight > maximum:
        maximum = weight
    if weight < minimum:
        minimum = weight
print(minimum, maximum)   
"""
"""  3 вариант:
n = int(input('Введите количество арбузов: '))

numbers = []
for i in range(n):
    weight = int(input('Введите массу арбуза: '))
    numbers.append(weight)
print(max(numbers), min(numbers))
"""
""" 4 вариант:"""
n = int(input('Введите количество арбузов: '))
weight = int(input('Введите массу арбуза: '))
minimum = weight
maximum = weight
for i in range(n-1):
    weight = int(input('Введите массу арбуза: '))
    maximum = max(maximum, weight)
    minimum = min(minimum, weight)
print(minimum, maximum)   
