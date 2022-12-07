from collections import defaultdict
import functools
import math
import numpy as np
math_dir = defaultdict(list)
def calculator():
    calcresult = float()
    x = float(input("Введите первое число "))
    y = float(input("Введите второе число "))
    z = (input("Введите действие "))
    if z == "*" :    
            calcresult = (x*y)
            math_dir["Умножение"].append(calcresult)
    elif z == "/" :
            calcresult = (x/y)
            math_dir["Деление"].append(calcresult)
    elif z == "-":
            calcresult = (x - y)
            math_dir["Вычитание"].append(calcresult)
    elif z == "+": 
            calcresult = (x + y)
            math_dir["Сумма"].append(calcresult)
    return calcresult
def math_array():
    array_length=len(array)
    mathDo = (input("Введите действие "))
    Elements = int()
    for i in range(array_length):
        if mathDo == "+":
            Elements=sum(array)
            math_dir["Сумма всех чисел"]=[Elements]
        elif mathDo == "*":
            Elements=math.prod(array)
            math_dir["Умножение всех чисел"]=[Elements]
        elif mathDo == "/":
            Elements = array[0] / array[i]
            math_dir["Деление всех чисел"]=[Elements]
        elif mathDo == "-":
            Elements = array[0] - array[i]
            math_dir["Вычитание всех чисел"]= [Elements]
    return Elements
array_size = int(input('Сколько операций?'))
array = []
while array !=0:
    calcresult=calculator()
    array.append(float(calcresult))
    array_size = array_size - 1
    if array_size == 0:
        break
array_length=len(array)
Elements = math_array()
for k, v in math_dir.items():
    print(f"{k} >>> {v}")
