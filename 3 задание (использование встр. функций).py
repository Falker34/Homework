#SERIES26
K = int(input("Введите число K: "))
N = int(input("Введите число N: "))

def fill(n):
    kna = []
    while len(kna) != N:
        kna.append(float(input("Введите число из набора: ")))
    return kna

def count(list, k):
    kna = []
    for n in list:
        n = n ** k
        kna.append(n)
    return kna

print(count(fill(N),K))
print("Выше написан преобразованный набор")

#WHILE30
def times(x):
    return x-C >= C #функция

A= int(input("Введите число A:"))
B= int(input("Введите число B:"))
C= int(input("Введите число C:"))
n = 1
m = 1
vsp = 1
if B < C or A < C:
    print("В такой прямоугольник не поместиться ни одного квадрата со стороной C.")
else:
    while times(A): #Применяю функцию
        A= A-C
        n+= 1
    while times(B): #Применяю функцию
        B= B-C
        m+= 1
    k = m
    while vsp != n: #Считаем произведение не прибегая к операции умножения
        k = k + m
        vsp+= 1
    print("Кол-во квадратов со стороной C умещающихся на прямоугольнике со сторонами A и B равно: ", k)
