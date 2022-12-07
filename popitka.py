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
array_size = int(input('Сколько операций?'))
array = []
while array !=0:
    calcresult=calculator()
    array.append(float(calcresult))
    array_size = array_size - 1
    if array_size == 0:
        break
array_length=len(array)
for k, v in math_dir.items():
    print(f"{k} >>> {v}")
