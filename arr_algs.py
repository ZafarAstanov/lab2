massive=[] #создаем массив, в которой нужно будет указать кол-во цифр
for i in range(int(input())):
    massive.append(int(input()))

# В перменной "К" зранится индекс элемента, подлежащего обмену (двигаемся слева на право)

def minimum(massive): #Функция для вычисления минимумма
    minmas = massive[0]
    for i in massive:
        if i < minmas:
            minmas = i
    return minmas

def average(massive): #Функция для вычисления среднегоо арифм. числа
    s=0
    for x in massive:
         s += x
    return s/len(massive)

#вывод на экран
print(minimum(massive))
print(average(massive))
