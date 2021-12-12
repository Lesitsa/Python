import math

# №1 Два числа
try:
    number_1 = float(input('Введите первое число: '))
    number_2 = float(input('Введите второе число: '))
except:
    print('Некорректный ввод - используйте только вещественные и целочисленные числа!')
    exit()
print(f'Сумма {number_1} и {number_2} равна {number_1 + number_2} \n'
      f'Разность {number_1} и {number_2} равна {number_1 - number_2} \n'
      f'Разность {number_2} и {number_1} равна {number_2 - number_1} \n'
      f'Произведение {number_1} и {number_2} равно {number_1 * number_2} \n'
      f'Деление {number_1} и {number_2} равно {number_1 / number_2 if number_2 != 0 else "  !На 0 делить нельзя!"} \n'
      f'Деление {number_2} и {number_1} равно {number_2 / number_1 if number_1 != 0 else "  !На 0 делить нельзя!"} \n'
      f'{number_1} в степени {number_2} равно {number_1 ** number_2 if number_2 >= 0 and number_1 != 0 else "  !Возводить 0 в отрицательную степень нельзя!"} \n'
      f'{number_2} в степени {number_1} равно {number_2 ** number_1 if number_1 >= 0 and number_2 != 0 else "  !Возводить 0 в отрицательную степень нельзя!"} \n'
      f'|{number_1}| / |{number_2}| равно {abs(number_1) / abs(number_2) if number_2 != 0 else "  !На 0 делить нельзя!"} \n'
      f'|{number_2}| / |{number_1}| равно {abs(number_2) / abs(number_1) if number_1 != 0 else "  !На 0 делить нельзя!"} \n'
      f'Целочисленное деление {number_1} и {number_2} равно {number_1 // number_2 if number_2 != 0 else "  !На 0 делить нельзя!"} \n'
      f'Целочисленное деление {number_2} и {number_1} равно {number_2 // number_1 if number_1 != 0 else "  !На 0 делить нельзя!"} \n')

# №2 Поздороваться по имени
name = input('Введите имя: ')
print(f'Добрый день, {name}! \n')

# №3 Последние 2 символа
line = input('Введите строку: ')[::-1]
print(f'Последние 2 символа этой строки в обратном порядке: {line[:2] if len(line) >= 2 else "  Ошибка! Строка содержит менее 2ух символов."} \n')

# №4 Площадь круга
try:
    R = float(input('Введите радиус круга: '))
except:
    print('Некорректный ввод - используйте только вещественные и целочисленные числа!')
    exit()
print(f'Площадь круга равна {math.pi * R**2 if R >= 0 else " Ошибка! Радиус не может быть отрицательным."}')