def calculator():
    calcresult = float()
    x = float(input("Введите первое число "))
    y = float(input("Введите второе число "))
    z = (input("Введите действие "))
    if z == "*" :
            calcresult = (x*y)
    elif z == "/" :
            calcresult = (x/y)
    elif z == "-":
            calcresult = (x - y)
    elif z == "+":
            calcresult = (x + y)
    return calcresult
def math_array():
    array_length=len(array)
    Elements=0
    mathDo = (input("Введите действие "))
    for i in range(array_length):
        if mathDo == "+":
            Elements=array[i] + array[i-1]
        elif mathDo == "*":
            Elements=array[i] * array[i-1]
        elif mathDo == "/":
            Elements=array[i] / array[i-1]
        elif mathDo == "-":
            Elements=array[i] - array[i-1]
    return Elements
array_size = int(input('Сколько чисел в массиве?'))
array = []
while array !=0:
    calcresult=calculator()
    array.append(float(calcresult))
    array_size = array_size - 1
    if array_size == 0:
        break
print(array)
array_length=len(array)
Elements = math_array() 
print(Elements)
