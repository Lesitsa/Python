from os import getlogin, listdir, name
import numpy as np
from numpy.random.mtrand import f
from func_test import check_number, fibonacci

'''№4 Библиотека os
Подключение библиотеки os.
Вывод с её помощью: 
имя операционной системы;
имя пользователя, вошедшего в терминал;
список файлов и директорий в папке.
'''
print('№4 Библиотека os \n')
print(f'Имя операционной системы: {name}, \n'
      f'Имя пользователя, вошедшего в терминал: {getlogin()}, \n'
      f'Список файлов и директорий в папке: \n{", ".join(map(str, listdir(path=".")))} \n')

'''№5 Библиотека numpy&массив
Создание с помощью библиотеки numpy массива 3x3 со случайными значениями.
Вывод исходного и транспонированного массива.
'''
matrix = np.random.random((3, 3))
matrix *= 100
print('№5 Библиотека numpy&массив \n')
print(f'Исходный массив: \n{matrix} \n'
      f'Транспонированный массив: \n{matrix.transpose()} \n')

'''№6 Функция Фибоначчи
Возвращает заданное число Фибоначчи
'''
print('№6 Число Фибоначчи \n')
print(f'Это число: {fibonacci(check_number())}')
