array_size = int(input('Сколько чисел в массиве?'))
array = []
while array !=0:
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
    array.append(int(calcresult))
    array_size = array_size - 1
    carcresult = float()
    if array_size == 0:
        break
print(array)
array_length=len(array)
Elements=0
mathDo = (input("Введите действие "))
for i in range(array_length):
    calcresult = float()
    if mathDo == "+":
        Elements=Elements+array[i]
    elif mathDo == "*":
        Elements=Elements*array[i]
    elif mathDo == "/":
        Elements=Elements/array[i]
    elif mathDo == "-":
        Elements=Elements-array[i]    
print(Elements)
