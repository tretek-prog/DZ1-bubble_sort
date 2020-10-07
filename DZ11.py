#Вводим через пробел наши числа
a = [int(el) for el in input().split()]

def bubble_sort(a):
    k = True #Посколько значиние = true, цикл выполниться хотя бы один раз ( вдруг требутеся соврешить лишь одну перестоновку)
    while k:
        k =  False
        for i in range(len(a) - 1):
            if a[i] > a[i+1]: # Меняем местами,если больше.
                a[i],a[i+1] = a[i+1],a[i]
                k = True
bubble_sort(a) #присваиваем новое значение а
print(a)
