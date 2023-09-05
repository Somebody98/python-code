print('Введите числа для решения уравнения через дискриминант ')
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = b ** 2 - 4 * a * c
m = d **0.5
print ("Дискриминант равен =", (d))
if d<0:
    print('Корней нет')
if d == 0:
    f = (-b + m) / (2*a)
    print("x1 = ",f)
if d > 0:
    f = (-b + m) / (2*a)
    print ("x1 = ",f)
    ff = (-b - m)/ (2*a)
    print ("x2 = ",ff)