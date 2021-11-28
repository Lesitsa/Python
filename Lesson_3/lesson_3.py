import math
import cmath

# №1 Движение по координатной оси
x, y = 0, 0
print(f'Текущие координаты ({x},{y})')
try:
    route, number = input('Ведите через пробел данные для движения (в-вверх, н-вниз, л-влево, п-вправо), например, н 5 : ').split(' ')
    if route.lower() == 'в':
        y += int(number)
    elif route.lower() == 'н':
        y -= int(number)
    elif route.lower() == 'л':
        x -= int(number)
    elif route.lower() == 'п':
        x += int(number)
    else:
        exit()
except:
    print('Данные введены некорректно - используйте только в/н/л/п и целое число')
    exit()
print(f'Текущие координаты ({x},{y}) \n')

# №2 Бесконечное движение по координатной оси
x, y = 0, 0
print(f'Текущие координаты ({x},{y})\n'
'Чтобы завершить игру введите "стоп"')
while 1:
    try:
        route_number = input('Ведите через пробел данные для движения (в-вверх, н-вниз, л-влево, п-вправо), например, н 5 : ').split(' ')
        route = route_number[0]
        if route.lower() == 'стоп':
            print('Игра закончена \n')
            break
        number = route_number[1]   
        if route.lower() == 'в':
            y += int(number)
        elif route.lower() == 'н':
            y -= int(number)
        elif route.lower() == 'л':
            x -= int(number)
        elif route.lower() == 'п':
            x += int(number)
        else:
            exit()
    except:
        print('Данные введены некорректно - используйте только в/н/л/п и целое число')
        exit()
    print(f'Текущие координаты ({x},{y})')

# №3 и №4 Решение квадратного уравнения (с комплексными числами)
try:
    a, b, c = input('Введите коэффициенты для уравнения ax^2+bx+c=0 через пробел: ').split(' ')
    a, b, c = float(a), float(b), float(c)
    if a == 0:
        print('Уравнение не является квадратным')
        exit()
except:
    print('Данные введены некорректно')
    exit()
D = b**2 - 4*a*c
if D > 0:
    print(f'Корни квадратного уравнения равны {(-b + math.sqrt(D)) / (2*a)} и {(-b - math.sqrt(D)) / (2*a)}')
elif D == 0:
    print(f'Корень квадратного уравнения равен {-b / (2*a)}')
else:
    print(f'Корни квадратного уравнения равны {(-b + complex(cmath.sqrt(D))) / (2*a)} и {(-b - complex(cmath.sqrt(D))) / (2*a)}')